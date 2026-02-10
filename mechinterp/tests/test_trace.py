import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

import numpy as np

from trm_trace.trace import TraceReader, TraceWriter, validate_step_schema


class TraceSchemaTests(unittest.TestCase):
    def test_validate_step_schema_missing(self):
        with self.assertRaises(ValueError):
            validate_step_schema({"t": 0, "h": [0.0], "aux": {}, "y": 0.1})

    def test_write_and_read_jsonl(self):
        out = Path("tools/bench/out/tests/trace_test.jsonl")
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            out.unlink()

        with TraceWriter(path=out, task_id="task_x", seed=3, fmt="jsonl") as writer:
            writer.add_step(t=0, h=np.array([1.0, 2.0]), aux={"a": np.array([0.5])}, y=0.8, metrics={"ok": 1})

        record = TraceReader(out).read()
        self.assertEqual(record.task_id, "task_x")
        self.assertEqual(record.seed, 3)
        self.assertEqual(record.steps[0]["t"], 0)


if __name__ == "__main__":
    unittest.main()
