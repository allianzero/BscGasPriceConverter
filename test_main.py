"""Tests for BscGasPriceConverter."""
import unittest
from main import calculate


class TestTool(unittest.TestCase):
    def test_main_function(self):
        self.assertAlmostEqual(calculate(5), 5000000000.0, places=6)


if __name__ == "__main__":
    unittest.main()
