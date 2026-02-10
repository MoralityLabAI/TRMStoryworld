import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

import numpy as np

from analysis.sae import fit_sae, sae_metrics, sae_stability


class SAETests(unittest.TestCase):
    def test_fit_and_metrics(self):
        rng = np.random.default_rng(1)
        states = rng.normal(size=(128, 12)).astype(np.float32)
        sae = fit_sae(states, feature_dim=24, k=4, steps=250, seed=2)
        metrics = sae_metrics(states, sae)
        self.assertIn("recon_mse", metrics)
        self.assertGreaterEqual(metrics["mean_nnz"], 0.0)
        self.assertLessEqual(metrics["dead_feature_frac"], 1.0)

    def test_stability(self):
        rng = np.random.default_rng(4)
        states = rng.normal(size=(96, 10)).astype(np.float32)
        score = sae_stability(
            states,
            config={"feature_dim": 18, "k": 3, "lr": 1e-2, "steps": 200, "batch_size": 64, "l1_coeff": 1e-3},
            seed_a=0,
            seed_b=1,
        )
        self.assertIn("mean_abs_feature_match_corr", score)
        self.assertGreaterEqual(score["mean_abs_feature_match_corr"], 0.0)
        self.assertLessEqual(score["mean_abs_feature_match_corr"], 1.0)


if __name__ == "__main__":
    unittest.main()
