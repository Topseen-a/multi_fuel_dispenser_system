import unittest

from multi_fuel_dispenser_system.fuel import Fuel


class FuelTest(unittest.TestCase):

    def setUp(self):
        self.fuel = Fuel("Petrol", 840, 50)

    def test_that_fuel_type_is_set_correctly(self):
        self.assertEqual("Petrol", self.fuel.fuel_type)

    def test_that_price_per_liter_is_set_correctly(self):
        self.assertEqual(840, self.fuel.price_per_liter)

    def test_that_quantity_is_set_correctly(self):
        self.assertEqual(50, self.fuel.quantity)

    def test_that_empty_fuel_type_raises_error(self):
        with self.assertRaises(ValueError):
            Fuel("", 840, 50)

    def test_that_price_less_than_or_equal_zero_raises_error(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 0, 50)

    def test_that_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 840, -10)
