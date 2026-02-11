#!/usr/bin/env python3
"""Run a long TRM/HRM command with hard safety rails.

Safety rails:
- Single-instance lock file.
- Explicit authorization gate.
- Real-time stdout/stderr streaming to console and log file.
- RSS watchdog with clean shutdown on pressure.
- Heartbeat JSONL with timestamp/step/rss/pid metadata.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import psutil
except Exception:  # pragma: no cover
    psutil = None  # type: ignore[assignment]


AUTH_TOKEN = "I_UNDERSTAND_THIS_STARTS_TRAINING"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Guarded launcher for long training commands.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--command", required=True, help="Command to run, quoted as one string.")
    parser.add_argument("--cwd", default=".", help="Working directory for the command.")
    parser.add_argument("--log-dir", default="negotiation-storyworld/logs", help="Output log directory.")
    parser.add_argument("--run-id", default="", help="Optional run id. Auto-generated if omitted.")
    parser.add_argument("--lock-file", default="", help="Optional lock file path.")
    parser.add_argument("--max-ram-pct", type=float, default=85.0, help="RSS limit as percent of total RAM.")
    parser.add_argument("--check-every-seconds", type=float, default=5.0, help="Memory check interval.")
    parser.add_argument("--heartbeat-seconds", type=float, default=30.0, help="Heartbeat interval.")
    parser.add_argument(
        "--graceful-timeout-seconds",
        type=float,
        default=20.0,
        help="Wait after terminate before hard kill.",
    )
    parser.add_argument(
        "--authorize",
        default="",
        help=f"Must be exactly '{AUTH_TOKEN}' or launcher exits.",
    )
    return parser.parse_args()


def _pid_alive(pid: int) -> bool:
    if pid <= 0:
        return False
    if psutil is not None:
        return psutil.pid_exists(pid)
    if os.name == "nt":
        # Fallback without psutil.
        out = subprocess.run(
            ["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            check=False,
        )
        line = (out.stdout or "").strip()
        return bool(line and "No tasks are running" not in line)
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def acquire_lock(lock_path: Path, run_meta: Dict[str, Any]) -> None:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    if lock_path.exists():
        stale = True
        try:
            existing = json.loads(lock_path.read_text(encoding="utf-8"))
            stale = not _pid_alive(int(existing.get("pid") or -1))
        except Exception:
            stale = True
        if stale:
            lock_path.unlink(missing_ok=True)
        else:
            raise RuntimeError(f"Lock exists: {lock_path}")
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    fd = os.open(str(lock_path), flags)
    try:
        os.write(fd, json.dumps(run_meta, indent=2).encode("utf-8"))
    finally:
        os.close(fd)


def release_lock(lock_path: Path) -> None:
    lock_path.unlink(missing_ok=True)


def format_gb(num_bytes: float) -> float:
    return round(num_bytes / (1024 ** 3), 3)


def process_tree_rss(proc: "psutil.Process") -> int:
    if psutil is None:
        return 0
    total = 0
    procs: List["psutil.Process"] = [proc]
    try:
        procs.extend(proc.children(recursive=True))
    except Exception:
        pass
    for item in procs:
        try:
            total += int(item.memory_info().rss)
        except Exception:
            continue
    return total


def terminate_process(process: subprocess.Popen[str], timeout_s: float) -> None:
    if process.poll() is not None:
        return
    try:
        if os.name == "nt":
            process.terminate()
        else:
            process.send_signal(signal.SIGTERM)
        process.wait(timeout=timeout_s)
        return
    except Exception:
        pass
    if process.poll() is None:
        process.kill()
        try:
            process.wait(timeout=5)
        except Exception:
            pass


def stream_output(process: subprocess.Popen[str], run_log_path: Path, stop_event: threading.Event) -> None:
    with run_log_path.open("a", encoding="utf-8", buffering=1) as log_handle:
        for line in iter(process.stdout.readline, ""):
            if not line:
                break
            text = line.rstrip("\n")
            ts_line = f"[{now_iso()}] {text}"
            print(ts_line, flush=True)
            log_handle.write(ts_line + "\n")
            if stop_event.is_set():
                break


def main() -> int:
    args = parse_args()
    if args.authorize != AUTH_TOKEN:
        print(
            f"Refusing to start training. Pass --authorize \"{AUTH_TOKEN}\" to proceed.",
            file=sys.stderr,
        )
        return 2
    if psutil is None:
        print("psutil is required for RSS watchdog. Install with: pip install psutil", file=sys.stderr)
        return 2
    if not (0 < args.max_ram_pct < 100):
        print("--max-ram-pct must be between 0 and 100.", file=sys.stderr)
        return 2

    run_id = args.run_id.strip() or f"guarded-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    run_log_path = log_dir / f"{run_id}.log"
    heartbeat_path = log_dir / f"{run_id}_heartbeat.jsonl"
    lock_path = Path(args.lock_file) if args.lock_file else (log_dir / "trm_training.lock")
    command_list = shlex.split(args.command, posix=os.name != "nt")
    run_meta = {
        "run_id": run_id,
        "pid": os.getpid(),
        "command": command_list,
        "cwd": str(Path(args.cwd).resolve()),
        "started_at": now_iso(),
        "max_ram_pct": args.max_ram_pct,
        "log_path": str(run_log_path),
    }

    try:
        acquire_lock(lock_path, run_meta)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    stop_event = threading.Event()
    start_ts = time.time()
    process: Optional[subprocess.Popen[str]] = None
    try:
        env = os.environ.copy()
        env["PYTHONUNBUFFERED"] = "1"
        env["PYTHONIOENCODING"] = "utf-8"
        with run_log_path.open("a", encoding="utf-8", buffering=1) as log_handle:
            log_handle.write(json.dumps({"event": "start", **run_meta}, ensure_ascii=True) + "\n")
        process = subprocess.Popen(
            command_list,
            cwd=args.cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            env=env,
        )
        proc = psutil.Process(process.pid)
        stream_thread = threading.Thread(
            target=stream_output,
            args=(process, run_log_path, stop_event),
            daemon=True,
        )
        stream_thread.start()

        vm = psutil.virtual_memory()
        threshold_bytes = int((args.max_ram_pct / 100.0) * vm.total)
        next_heartbeat = 0.0
        while process.poll() is None:
            elapsed = time.time() - start_ts
            rss = process_tree_rss(proc)
            if elapsed >= next_heartbeat:
                heartbeat = {
                    "ts": now_iso(),
                    "run_id": run_id,
                    "pid": process.pid,
                    "rss_gb": format_gb(float(rss)),
                    "rss_pct_total": round((rss / vm.total) * 100.0, 2),
                    "uptime_sec": round(elapsed, 1),
                }
                with heartbeat_path.open("a", encoding="utf-8", buffering=1) as hb:
                    hb.write(json.dumps(heartbeat, ensure_ascii=True) + "\n")
                    hb.flush()
                next_heartbeat = elapsed + args.heartbeat_seconds
            if rss > threshold_bytes:
                msg = {
                    "event": "memory_threshold_exceeded",
                    "ts": now_iso(),
                    "run_id": run_id,
                    "pid": process.pid,
                    "rss_gb": format_gb(float(rss)),
                    "threshold_pct": args.max_ram_pct,
                }
                with run_log_path.open("a", encoding="utf-8", buffering=1) as log_handle:
                    log_handle.write(json.dumps(msg, ensure_ascii=True) + "\n")
                    log_handle.flush()
                print(json.dumps(msg, ensure_ascii=True), flush=True)
                terminate_process(process, timeout_s=args.graceful_timeout_seconds)
                break
            time.sleep(max(0.2, args.check_every_seconds))

        stop_event.set()
        stream_thread.join(timeout=2.0)
        rc = process.wait(timeout=5) if process is not None else 1
        end_meta = {
            "event": "end",
            "ts": now_iso(),
            "run_id": run_id,
            "return_code": rc,
            "duration_sec": round(time.time() - start_ts, 2),
        }
        with run_log_path.open("a", encoding="utf-8", buffering=1) as log_handle:
            log_handle.write(json.dumps(end_meta, ensure_ascii=True) + "\n")
        return int(rc)
    finally:
        release_lock(lock_path)


if __name__ == "__main__":
    raise SystemExit(main())
