import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

from runner.run_tasks import run_tasks


class DeterminismTests(unittest.TestCase):
    def _hash_file(self, path: Path) -> str:
        data = path.read_bytes()
        return hashlib.sha256(data).hexdigest()

    def test_fixed_seed_equivalence(self):
        out1 = Path("tools/bench/out/tests/det_run_1")
        out2 = Path("tools/bench/out/tests/det_run_2")
        summary1 = run_tasks(out_dir=out1, num_tasks=5, steps=4, seed=123, fmt="jsonl", compress=False)
        summary2 = run_tasks(out_dir=out2, num_tasks=5, steps=4, seed=123, fmt="jsonl", compress=False)

        rows1 = json.loads(summary1.read_text(encoding="utf-8"))
        rows2 = json.loads(summary2.read_text(encoding="utf-8"))

        self.assertEqual(len(rows1), len(rows2))
        for i in range(len(rows1)):
            p1 = Path(rows1[i]["trace_path"])
            p2 = Path(rows2[i]["trace_path"])
            self.assertEqual(self._hash_file(p1), self._hash_file(p2))


if __name__ == "__main__":
    unittest.main()
