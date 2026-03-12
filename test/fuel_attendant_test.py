import unittest

from multi_fuel_dispenser_system.dispenser import Dispenser
from multi_fuel_dispenser_system.fuel_attendant import FuelAttendant
from multi_fuel_dispenser_system.fuel import Fuel


class FuelAttendantTest(unittest.TestCase):

    def setUp(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Tayo Ade", self.dispenser)
        self.fuel = Fuel("Petrol", 840, 50)

    def test_that_dispenser_is_empty_at_initial(self):
        self.assertEqual(0, len(self.dispenser.fuels))

    def test_that_attendant_can_add_new_fuel(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.attendant.add_new_fuel("Gas", 1000, 50)

        fuel = self.dispenser.get_fuel("Gas")

        self.assertEqual("Gas", fuel.fuel_type)
        self.assertEqual(1000, fuel.price_per_liter)
        self.assertEqual(50, fuel.quantity)

    def test_that_attendant_can_get_all_available_fuels(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        self.attendant.add_new_fuel("Gas", 1000, 50)

        fuels = self.attendant.get_available_fuels()

        self.assertIn("Petrol", fuels)
        self.assertEqual(840, fuels["Petrol"]["price_per_liter"])
        self.assertEqual(50, fuels["Petrol"]["quantity"])

        self.assertIn("Gas", fuels)
        self.assertEqual(1000, fuels["Gas"]["price_per_liter"])
        self.assertEqual(50, fuels["Gas"]["quantity"])

    def test_that_attendant_can_update_fuel_price(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        self.attendant.update_fuel_price("Petrol", 900)
        fuel = self.dispenser.get_fuel("Petrol")

        self.assertEqual(900, fuel.price_per_liter)

    def test_that_attendant_can_restock_fuel(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        self.attendant.restock_fuel("Petrol", 50)
        fuel = self.dispenser.get_fuel("Petrol")

        self.assertEqual(100, fuel.quantity)

    def test_that_attendant_can_dispense_fuel_by_liters(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        transaction = self.attendant.dispense_by_liters("Petrol", 10)

        self.assertEqual(1, len(self.attendant.transactions))
        self.assertEqual("Petrol", transaction["fuel"])
        self.assertEqual(10, transaction["liters"])
        self.assertEqual(8400, transaction["amount"])

    def test_that_attendant_can_dispense_fuel_by_amount(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        transaction = self.attendant.dispense_by_amount("Petrol", 8400)

        self.assertEqual(1, len(self.attendant.transactions))
        self.assertEqual("Petrol", transaction["fuel"])
        self.assertEqual(10, transaction["liters"])
        self.assertEqual(8400, transaction["amount"])

    def test_that_transactions_can_be_viewed(self):
        self.assertEqual(0, len(self.dispenser.fuels))

        self.dispenser.add_fuel(self.fuel)
        self.attendant.dispense_by_liters("Petrol", 5)
        transactions = self.attendant.show_transactions()

        self.assertEqual(1, len(transactions))