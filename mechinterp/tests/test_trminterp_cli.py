import os
import subprocess
import sys
from pathlib import Path

import unittest


ROOT = Path(__file__).resolve().parents[1]


class TRMInterpCLITests(unittest.TestCase):
    def test_trace_sae_intervene_pipeline(self):
        run_dir = ROOT / "tools" / "bench" / "out" / "tests" / "trminterp_smoke"
        run_dir.mkdir(parents=True, exist_ok=True)
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT / "src")

        subprocess.run(
            [
                sys.executable,
                "-m",
                "trminterp",
                "trace",
                "--run-dir",
                str(run_dir),
                "--num-tasks",
                "6",
                "--steps",
                "4",
                "--seed",
                "17",
                "--states-npy",
            ],
            check=True,
            env=env,
        )

        subprocess.run(
            [
                sys.executable,
                "-m",
                "trminterp",
                "sae",
                "fit",
                "--run-dir",
                str(run_dir),
                "--feature-dim",
                "16",
                "--k",
                "4",
                "--train-steps",
                "80",
            ],
            check=True,
            env=env,
        )

        subprocess.run(
            [
                sys.executable,
                "-m",
                "trminterp",
                "intervene",
                "--run-dir",
                str(run_dir),
                "--seed",
                "17",
                "--steps",
                "4",
                "--patch-step",
                "1",
                "--policy",
                "patch",
                "--top-k",
                "3",
            ],
            check=True,
            env=env,
        )

        self.assertTrue((run_dir / "trace.jsonl").exists())
        self.assertTrue((run_dir / "sae.pt").exists())
        self.assertTrue((run_dir / "sae_metrics.json").exists())
        self.assertTrue((run_dir / "report.json").exists())
        self.assertTrue((run_dir / "intervention_diffs.json").exists())


if __name__ == "__main__":
    unittest.main()
