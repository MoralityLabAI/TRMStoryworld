#!/usr/bin/env python3
"""Generate deterministic SW1 PICK traces, receipts, and benchmark summaries."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from env import DiplomacyStoryworldEnv, load_storyworld


def stable_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def h_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def h_bytes(left: bytes, right: bytes) -> bytes:
    return hashlib.sha256(left + right).digest()


def merkle_root_hex(leaves_hex: List[str]) -> str:
    if not leaves_hex:
        return h_hex("EMPTY")
    level = [bytes.fromhex(x) for x in leaves_hex]
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])
        nxt = []
        for i in range(0, len(level), 2):
            nxt.append(h_bytes(level[i], level[i + 1]))
        level = nxt
    return level[0].hex()


def q_i16(value: float, scale: int = 1000) -> int:
    return int(round(float(value) * scale))


def action_to_label(action: Dict[str, Any]) -> str:
    atype = action.get("type", "wait")
    target = action.get("target")
    return atype.upper() if not target else f"{atype.upper()} {target}"


def mk_leaf(
    episode_idx: int,
    turn: int,
    state_hash: str,
    pick_idx: int,
    k_budget: int,
    out_hash: str,
) -> str:
    payload = f"SW1D|{episode_idx}|{turn}|{state_hash}|{pick_idx}|{k_budget}|{out_hash}"
    return h_hex(payload)


def node_map(world: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return {node.get("id"): node for node in world.get("nodes", []) if isinstance(node, dict)}


def list_targets(world: Dict[str, Any], focal_agent: str) -> List[str]:
    targets = []
    for agent in world.get("agents", []):
        aid = agent.get("id")
        if aid and aid != focal_agent:
            targets.append(aid)
    return sorted(targets)


def build_choice_actions(targets: List[str]) -> List[Dict[str, Any]]:
    choices: List[Dict[str, Any]] = [{"type": "wait"}]
    for action_type in ("propose", "ally", "betray"):
        for target in targets:
            choices.append({"type": action_type, "target": target})
    return choices


def world_step_prompt(
    world: Dict[str, Any],
    nmap: Dict[str, Dict[str, Any]],
    state: Dict[str, Any],
    focal_agent: str,
    choice_actions: List[Dict[str, Any]],
) -> str:
    active = state.get("active_node")
    node = nmap.get(active, {})
    label = node.get("label", active or "unknown")
    tension = q_i16(node.get("state_vars", {}).get("tension", 0.0))
    turn = int(state.get("turn", 0))
    coalitions = state.get("coalitions", [])
    coal_min = []
    for coalition in coalitions:
        members = sorted(coalition.get("members", []))
        coal_min.append({"m": members, "s": q_i16(coalition.get("stability", 0.0))})
    beliefs = state.get("beliefs", {})
    targets = list_targets(world, focal_agent)
    trust_lines = []
    for target in targets:
        a_to_t = q_i16(beliefs.get(focal_agent, {}).get("trust", {}).get(target, 0.0))
        t_to_a = q_i16(beliefs.get(target, {}).get("trust", {}).get(focal_agent, 0.0))
        trust_lines.append(f"TR_{focal_agent}_{target}={a_to_t} TR_{target}_{focal_agent}={t_to_a}")
    choice_lines = []
    for idx, action in enumerate(choice_actions):
        label_text = action_to_label(action)
        choice_lines.append(f"{idx} {label_text}")
    parts = [
        "<SW1>",
        f"A={focal_agent} T={turn} NODE={label} TEN={tension}",
        f"COAL={stable_json(coal_min)}",
        *trust_lines,
        "CHOICES:",
        *choice_lines,
        "</SW1>",
    ]
    return "\n".join(parts)


@dataclass
class CandidateEval:
    pick_idx: int
    action: Dict[str, Any]
    score: int
    outcome: str
    metrics: Dict[str, Any]
    trust_inbound: int
    coalition_count: int
    coalition_stability: int
    latent_bonus: int
    latent_norm: float
    h_after: List[float]


def _action_type_id(action_type: str) -> int:
    order = {"wait": 0, "propose": 1, "ally": 2, "betray": 3}
    return int(order.get(action_type, 0))


def _target_bucket(world: Dict[str, Any], action: Dict[str, Any]) -> float:
    target = action.get("target")
    if not target:
        return 0.0
    targets = sorted([agent.get("id") for agent in world.get("agents", []) if agent.get("id")])
    if not targets:
        return 0.0
    idx = targets.index(target) if target in targets else 0
    return float(idx + 1) / float(max(1, len(targets)))


def _outcome_code(outcome: str) -> float:
    code = {"none": 0.0, "coalition": 0.33, "standoff": 0.66, "betrayal": 1.0}
    return float(code.get(outcome, 0.0))


def latent_features(
    world: Dict[str, Any],
    nmap: Dict[str, Dict[str, Any]],
    state: Dict[str, Any],
    focal_agent: str,
    action: Dict[str, Any],
    event: Dict[str, Any],
) -> np.ndarray:
    node = nmap.get(state.get("active_node"), {})
    turn = float(int(state.get("turn", 0)))
    tension = float(node.get("state_vars", {}).get("tension", 0.0))
    beliefs = state.get("beliefs", {})
    trust_inbound = 0.0
    for aid, belief in beliefs.items():
        if aid == focal_agent:
            continue
        trust_inbound += float(belief.get("trust", {}).get(focal_agent, 0.0))
    metrics = event.get("metrics", {})
    coalition_count = float(metrics.get("coalition_count") or 0.0)
    coalition_stability = float(metrics.get("coalition_mean_stability") or 0.0)
    action_type = float(_action_type_id(str(action.get("type", "wait")))) / 3.0
    target_bucket = _target_bucket(world, action)
    outcome_val = _outcome_code(str(event.get("outcome", "none")))
    vec = np.asarray(
        [
            turn / 10.0,
            tension,
            trust_inbound / 4.0,
            coalition_count / 4.0,
            coalition_stability,
            action_type,
            target_bucket,
            outcome_val,
        ],
        dtype=np.float32,
    )
    return vec


def latent_update(prev_h: np.ndarray, feat: np.ndarray) -> np.ndarray:
    dim = int(prev_h.shape[0])
    out = np.zeros((dim,), dtype=np.float32)
    for i in range(dim):
        base = float(prev_h[i])
        s1 = float(feat[i % feat.shape[0]])
        s2 = float(feat[(i * 3 + 1) % feat.shape[0]])
        bias = 0.1 * float(i + 1) / float(max(1, dim))
        out[i] = np.tanh(0.72 * base + 0.55 * s1 + 0.25 * s2 + bias)
    return out


def score_event(
    state_after: Dict[str, Any],
    event: Dict[str, Any],
    focal_agent: str,
    focal_action: Dict[str, Any],
) -> Tuple[int, Dict[str, int]]:
    beliefs = state_after.get("beliefs", {})
    targets = list(beliefs.keys())
    trust_inbound = 0
    for aid in targets:
        if aid == focal_agent:
            continue
        trust_inbound += q_i16(beliefs.get(aid, {}).get("trust", {}).get(focal_agent, 0.0))
    metrics = event.get("metrics", {})
    coalition_count = int(metrics.get("coalition_count") or 0)
    coalition_stability = q_i16(metrics.get("coalition_mean_stability") or 0.0)
    score = trust_inbound + (50 * coalition_stability) + (30 * coalition_count)
    if event.get("outcome") == "betrayal" and focal_action.get("type") == "betray":
        score -= 200_000
    comp = {
        "trust_inbound": trust_inbound,
        "coalition_count": coalition_count,
        "coalition_stability": coalition_stability,
    }
    return score, comp


def run_counterfactual(
    world: Dict[str, Any],
    base_state: Dict[str, Any],
    focal_agent: str,
    focal_action: Dict[str, Any],
    opponent_policy: str,
    episode_idx: int,
    turn: int,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    sim_env = DiplomacyStoryworldEnv(world, seed=0, log_path=None)
    sim_env.state = copy.deepcopy(base_state)
    all_agents = [a.get("id") for a in world.get("agents", []) if a.get("id")]
    actions = {}
    for aid in all_agents:
        if aid == focal_agent:
            actions[aid] = focal_action
        else:
            actions[aid] = scripted_opponent_action(
                world=world,
                aid=aid,
                focal_agent=focal_agent,
                opponent_policy=opponent_policy,
                episode_idx=episode_idx,
                turn=turn,
            )
    state_after, event, _done = sim_env.step(actions, [])
    return state_after, event


def best_recommendation(
    candidates: List[CandidateEval],
    action_type_set: Tuple[str, ...],
) -> Optional[CandidateEval]:
    filtered = [c for c in candidates if c.action.get("type") in action_type_set]
    if not filtered:
        return None
    return sorted(filtered, key=lambda c: (-c.score, c.pick_idx))[0]


def run_episode(
    world: Dict[str, Any],
    nmap: Dict[str, Dict[str, Any]],
    env_seed: int,
    focal_agent: str,
    max_steps: int,
    episode_idx: int,
    opponent_policy: str,
    latent_dim: int,
    latent_weight: float,
) -> Dict[str, Any]:
    env = DiplomacyStoryworldEnv(world, seed=env_seed, log_path=None)
    state = env.reset(seed=env_seed)
    targets = list_targets(world, focal_agent)
    choices = build_choice_actions(targets)
    leaf_hashes: List[str] = []
    steps: List[Dict[str, Any]] = []
    latent_steps: List[Dict[str, Any]] = []
    h = np.zeros((int(max(1, latent_dim)),), dtype=np.float32)
    for step_idx in range(max_steps):
        prompt = world_step_prompt(world, nmap, state, focal_agent, choices)
        state_hash = h_hex(stable_json(state))
        candidates: List[CandidateEval] = []
        for pick_idx, action in enumerate(choices):
            sim_state, sim_event = run_counterfactual(
                world=world,
                base_state=state,
                focal_agent=focal_agent,
                focal_action=action,
                opponent_policy=opponent_policy,
                episode_idx=episode_idx,
                turn=int(state.get("turn", 0)),
            )
            score, components = score_event(sim_state, sim_event, focal_agent, action)
            feat = latent_features(world, nmap, state, focal_agent, action, sim_event)
            h_after = latent_update(h, feat)
            latent_norm = float(np.linalg.norm(h_after))
            latent_bonus = int(round(float(latent_weight) * latent_norm * 1000.0))
            candidates.append(
                CandidateEval(
                    pick_idx=pick_idx,
                    action=action,
                    score=score + latent_bonus,
                    outcome=str(sim_event.get("outcome")),
                    metrics=sim_event.get("metrics", {}),
                    trust_inbound=components["trust_inbound"],
                    coalition_count=components["coalition_count"],
                    coalition_stability=components["coalition_stability"],
                    latent_bonus=latent_bonus,
                    latent_norm=latent_norm,
                    h_after=h_after.astype(np.float32).tolist(),
                )
            )

        best = sorted(candidates, key=lambda c: (-c.score, c.pick_idx))[0]
        coalition_rec = best_recommendation(candidates, ("ally", "propose"))
        defection_rec = best_recommendation(candidates, ("betray",))
        neutral_rec = best_recommendation(candidates, ("wait",))
        k_budget = 1 if (coalition_rec and defection_rec and coalition_rec.score - defection_rec.score > 5_000) else 2

        all_agents = [a.get("id") for a in world.get("agents", []) if a.get("id")]
        live_actions = {}
        for aid in all_agents:
            if aid == focal_agent:
                live_actions[aid] = best.action
            else:
                live_actions[aid] = scripted_opponent_action(
                    world=world,
                    aid=aid,
                    focal_agent=focal_agent,
                    opponent_policy=opponent_policy,
                    episode_idx=episode_idx,
                    turn=int(state.get("turn", 0)),
                )

        next_state, event, done = env.step(live_actions, [])
        feat_live = latent_features(world, nmap, state, focal_agent, best.action, event)
        h_before = h.copy()
        h = latent_update(h, feat_live)
        out_hash = h_hex(stable_json(event.get("outcome")))
        leaf = mk_leaf(episode_idx, int(state.get("turn", 0)), state_hash, best.pick_idx, k_budget, out_hash)
        leaf_hashes.append(leaf)

        p_val = ["trust_inbound", "coalition_stability"]
        p2_val = ["trust_inbound", "coalition_stability", "coalition_count"]
        decision_label = "coalition"
        if best.action.get("type") == "betray":
            decision_label = "defection"
        elif best.action.get("type") == "wait":
            decision_label = "hold"

        reasoning_interpret_log = {
            "decision_label": decision_label,
            "keyrings": {
                "pValue": [p_val],
                "p2Value": [p2_val],
            },
            "candidate_scores": [
                {
                    "pick": c.pick_idx,
                    "action": action_to_label(c.action),
                    "score": c.score,
                    "latent_bonus": c.latent_bonus,
                    "latent_norm": c.latent_norm,
                    "outcome": c.outcome,
                    "trust_inbound": c.trust_inbound,
                    "coalition_count": c.coalition_count,
                    "coalition_stability": c.coalition_stability,
                }
                for c in sorted(candidates, key=lambda c: c.pick_idx)
            ],
        }

        recommendations = []
        if coalition_rec:
            recommendations.append(
                {
                    "label": "coalition",
                    "pick": coalition_rec.pick_idx,
                    "action": action_to_label(coalition_rec.action),
                    "keyrings": {"pValue": [p_val], "p2Value": [p2_val]},
                }
            )
        if defection_rec:
            recommendations.append(
                {
                    "label": "defection",
                    "pick": defection_rec.pick_idx,
                    "action": action_to_label(defection_rec.action),
                    "keyrings": {"pValue": [p_val], "p2Value": [p2_val]},
                }
            )

        negotiation_diary = {
            "turn": int(state.get("turn", 0)),
            "action_label": action_to_label(best.action),
            "decision_label": decision_label,
            "k_budget": k_budget,
            "fallback_neutral_pick": None if neutral_rec is None else neutral_rec.pick_idx,
        }

        steps.append(
            {
                "episode": episode_idx,
                "turn": int(state.get("turn", 0)),
                "prompt": prompt,
                "label": f"PICK {best.pick_idx}",
                "k_label": f"K {k_budget}",
                "state_hash": state_hash,
                "receipt_leaf": leaf,
                "reasoning_interpret_log": reasoning_interpret_log,
                "negotiation_diary": negotiation_diary,
                "recommendations": recommendations,
                "opponent_policy": opponent_policy,
                "latent": {
                    "h_before": h_before.astype(np.float32).tolist(),
                    "h_after": h.astype(np.float32).tolist(),
                    "latent_bonus": int(best.latent_bonus),
                    "latent_norm": float(np.linalg.norm(h)),
                },
                "event": event,
            }
        )
        latent_steps.append(
            {
                "episode": episode_idx,
                "turn": int(state.get("turn", 0)),
                "t": step_idx,
                "h": h.astype(np.float32).tolist(),
                "aux": {
                    "h_before": h_before.astype(np.float32).tolist(),
                    "features": feat_live.astype(np.float32).tolist(),
                    "latent_bonus": int(best.latent_bonus),
                    "policy_weight": float(latent_weight),
                },
                "y": float(best.score),
                "metrics": {
                    "pick_idx": int(best.pick_idx),
                    "action": action_to_label(best.action),
                    "state_hash": state_hash,
                },
            }
        )
        state = next_state
        if done:
            break

    return {
        "episode": episode_idx,
        "trace_root": merkle_root_hex(leaf_hashes),
        "output_commitment": h_hex(
            stable_json(
                {
                    "episode": episode_idx,
                    "labels": [s["label"] for s in steps],
                    "final_event": steps[-1]["event"] if steps else {},
                    "trace_root": merkle_root_hex(leaf_hashes),
                }
            )
        ),
        "steps": steps,
        "latent_steps": latent_steps,
        "done": bool(state.get("done")),
        "final_outcome": steps[-1]["event"].get("outcome") if steps else None,
    }


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def summarize(episodes: List[Dict[str, Any]]) -> Dict[str, Any]:
    steps = 0
    done = 0
    outcomes: Dict[str, int] = {}
    coalition_recs = 0
    defection_recs = 0
    for ep in episodes:
        if ep.get("done"):
            done += 1
        for step in ep.get("steps", []):
            steps += 1
            labels = {rec.get("label") for rec in step.get("recommendations", [])}
            if "coalition" in labels:
                coalition_recs += 1
            if "defection" in labels:
                defection_recs += 1
        outcome = ep.get("final_outcome") or "none"
        outcomes[outcome] = outcomes.get(outcome, 0) + 1
    return {
        "episodes": len(episodes),
        "steps": steps,
        "completed_episodes": done,
        "outcomes": outcomes,
        "coalition_recommendation_steps": coalition_recs,
        "defection_recommendation_steps": defection_recs,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--world", type=str, required=True)
    parser.add_argument("--episodes", type=int, default=20)
    parser.add_argument("--max-steps", type=int, default=6)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--focal-agent", type=str, default="AgentA")
    parser.add_argument("--opponent-policy", choices=["wait", "ally-first", "mixed"], default="wait")
    parser.add_argument("--trace-out", type=str, default="logs/trm_sw1_traces.jsonl")
    parser.add_argument("--episode-out", type=str, default="logs/trm_sw1_episodes.jsonl")
    parser.add_argument("--latent-trace-out", type=str, default="logs/trm_sw1_latent_traces.jsonl")
    parser.add_argument("--summary-out", type=str, default="logs/trm_sw1_summary.json")
    parser.add_argument("--latent-dim", type=int, default=16)
    parser.add_argument("--latent-weight", type=float, default=0.0)
    return parser.parse_args()


def scripted_opponent_action(
    world: Dict[str, Any],
    aid: str,
    focal_agent: str,
    opponent_policy: str,
    episode_idx: int,
    turn: int,
) -> Dict[str, Any]:
    if opponent_policy == "wait":
        return {"type": "wait"}
    if opponent_policy == "ally-first":
        return {"type": "propose", "target": focal_agent}
    targets = sorted(
        [agent.get("id") for agent in world.get("agents", []) if agent.get("id") and agent.get("id") != aid]
    )
    if not targets:
        return {"type": "wait"}
    seed_base = f"{episode_idx}|{turn}|{aid}|{focal_agent}"
    mode = int(hashlib.sha256((seed_base + "|mode").encode("utf-8")).hexdigest()[:8], 16) % 4
    target_idx = int(hashlib.sha256((seed_base + "|target").encode("utf-8")).hexdigest()[:8], 16) % len(targets)
    target = targets[target_idx]
    if mode == 0:
        return {"type": "wait"}
    if mode == 1:
        return {"type": "propose", "target": target}
    if mode == 2:
        return {"type": "ally", "target": target}
    return {"type": "betray", "target": target}


def main() -> int:
    args = parse_args()
    world = load_storyworld(args.world)
    nmap = node_map(world)
    episodes = []
    trace_rows = []
    latent_trace_rows = []
    for idx in range(args.episodes):
        ep_seed = args.seed + idx
        ep = run_episode(
            world=world,
            nmap=nmap,
            env_seed=ep_seed,
            focal_agent=args.focal_agent,
            max_steps=args.max_steps,
            episode_idx=idx,
            opponent_policy=args.opponent_policy,
            latent_dim=args.latent_dim,
            latent_weight=args.latent_weight,
        )
        episodes.append(ep)
        for step in ep["steps"]:
            trace_rows.append(step)
        for step in ep["latent_steps"]:
            latent_trace_rows.append(step)

    trace_out = Path(args.trace_out)
    episode_out = Path(args.episode_out)
    latent_trace_out = Path(args.latent_trace_out)
    summary_out = Path(args.summary_out)
    write_jsonl(trace_out, trace_rows)
    write_jsonl(latent_trace_out, latent_trace_rows)
    write_jsonl(episode_out, [{"episode": ep["episode"], "trace_root": ep["trace_root"], "output_commitment": ep["output_commitment"], "done": ep["done"], "final_outcome": ep["final_outcome"]} for ep in episodes])

    summary = summarize(episodes)
    summary["latent_trace_out"] = str(latent_trace_out)
    summary["latent_dim"] = int(args.latent_dim)
    summary["latent_weight"] = float(args.latent_weight)
    summary_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
