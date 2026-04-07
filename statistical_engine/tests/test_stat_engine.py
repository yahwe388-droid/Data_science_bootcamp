import unittest
import math
from src.stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    def test_mean(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_mean(), 2)

    def test_median_even(self):
        self.assertEqual(StatEngine([1, 2, 3, 4]).get_median(), 2.5)

    def test_median_odd(self):
        self.assertEqual(StatEngine([1, 2, 3]).get_median(), 2)

    def test_mode(self):
        self.assertEqual(StatEngine([1, 1, 2, 2]).get_mode(), [1.0, 2.0])

    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_invalid_data(self):
        with self.assertRaises(TypeError):
            StatEngine([1, "a", 3])

    def test_standard_deviation(self):
        engine = StatEngine([2, 4, 6])
        self.assertAlmostEqual(
            engine.get_standard_deviation(is_sample=False),
            math.sqrt(8 / 3)
        )


if __name__ == "__main__":
    unittest.main()