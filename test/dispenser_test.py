import unittest
from multi_fuel_dispenser_system.dispenser import Dispenser
from multi_fuel_dispenser_system.fuel import Fuel


class DispenserTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.fuel = Fuel("Petrol", 840, 50)

    def test_that_dispenser_fuels_is_empty_initially(self):
        self.assertEqual(0, len(self.dispenser.fuels))

    def test_that_fuel_can_be_added_in_the_dispenser(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        diesel = Fuel("Diesel", 900, 70)
        self.dispenser.add_fuel(diesel)
        self.assertEqual(1, len(self.dispenser.fuels))

    def test_that_duplicate_fuel_cannot_be_added(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        diesel = Fuel("Diesel", 900, 70)
        self.dispenser.add_fuel(diesel)

        with self.assertRaises(ValueError):
            self.dispenser.add_fuel(Fuel("Diesel", 900, 70))

    def test_that_get_fuel_returns_correct_fuel(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        diesel = Fuel("Diesel", 900, 70)
        self.dispenser.add_fuel(diesel)

        fuel = self.dispenser.get_fuel("Diesel")

        self.assertEqual(diesel, fuel)

    def test_that_get_fuel_raises_error_if_not_found(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        gas = Fuel("Gas", 1000, 100)
        self.dispenser.add_fuel(gas)

        with self.assertRaises(ValueError):
            self.dispenser.get_fuel("Diesel")

    def test_that_get_available_fuels_returns_correct_data(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        gas = Fuel("Gas", 1000, 100)
        self.dispenser.add_fuel(gas)

        fuels = self.dispenser.get_available_fuels()

        self.assertEqual(
            {
                "Gas": {
                    "price_per_liter": 1000,
                    "quantity": 100
                }
            },
            fuels
        )