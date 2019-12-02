from unittest import TestCase

from day1.program import calculate_fuel, calculate_fuel_recursive


class TestProgram(TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(654, calculate_fuel(1969))
        self.assertEqual(33583, calculate_fuel(100756))

    def test_calculate_fuel_recursive(self):
        self.assertEqual(966, calculate_fuel_recursive(1969))
        self.assertEqual(50346, calculate_fuel_recursive(100756))
