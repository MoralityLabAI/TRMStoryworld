import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

import numpy as np

from analysis.sae import fit_sae
from trm_trace.interventions import ablate_aux, ablate_features, add_direction, clamp_features, patch_features, patch_state


class InterventionTests(unittest.TestCase):
    def test_patch_state_swaps_step(self):
        trace_a = {"steps": [{"h": np.array([0.0, 1.0], dtype=np.float32)}]}
        trace_b = {"steps": [{"h": np.array([3.0, 4.0], dtype=np.float32)}]}
        patched, log = patch_state(trace_a, trace_b, t=0)
        self.assertTrue(np.allclose(patched, np.array([3.0, 4.0], dtype=np.float32)))
        self.assertGreater(log["delta_l2"], 0.0)

    def test_add_direction(self):
        out, log = add_direction(np.array([1.0, 1.0]), np.array([0.5, -0.5]), alpha=2.0)
        self.assertTrue(np.allclose(out, np.array([2.0, 0.0])))
        self.assertGreater(log["delta_l2"], 0.0)

    def test_ablate_aux(self):
        aux = {"gate": np.array([1.0, 2.0]), "other": np.array([3.0])}
        out, log = ablate_aux(aux, keys=["gate"])
        self.assertTrue(np.allclose(out["gate"], np.zeros_like(aux["gate"])))
        self.assertEqual(log["count"], 1)

    def test_feature_ablate_clamp_patch(self):
        states = np.array(
            [
                [1.0, 0.0, 0.2, -0.1],
                [0.8, 0.1, 0.3, -0.2],
                [0.0, 1.0, -0.2, 0.1],
                [0.1, 0.9, -0.1, 0.2],
            ],
            dtype=np.float32,
        )
        sae = fit_sae(states, feature_dim=6, k=2, steps=200, seed=0)
        x = states[0]
        donor = states[2]

        ablated, log_a = ablate_features(x, sae=sae, feature_ids=[0, 1])
        self.assertEqual(log_a["type"], "ablate_features")
        self.assertEqual(ablated.shape, x.shape)

        clamped, log_c = clamp_features(x, sae=sae, feature_ids=[0, 1], values=[0.0, 0.25])
        self.assertEqual(log_c["type"], "clamp_features")
        self.assertEqual(clamped.shape, x.shape)

        patched, log_p = patch_features(x, donor_state=donor, sae=sae, feature_ids=[0, 1, 2])
        self.assertEqual(log_p["type"], "patch_features")
        self.assertEqual(patched.shape, x.shape)


if __name__ == "__main__":
    unittest.main()
