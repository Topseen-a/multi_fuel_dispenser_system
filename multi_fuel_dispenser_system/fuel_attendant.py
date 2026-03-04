from multi_fuel_dispenser_system.dispenser import Dispenser
from datetime import datetime

class FuelAttendant:
    def __init__(self, full_name, dispenser):
        self.full_name = full_name
        self.dispenser = dispenser

    def dispense_fuel_by_liters(self, fuel_type, liters):
        fuel = self.dispenser.get_fuel(fuel_type)
        liters_dispensed, total_cost = fuel.dispense_by_liters(liters)

        transaction = {
            "attendant": self.full_name,
            "fuel": fuel_type,
            "liters": liters_dispensed,
            "total_cost": total_cost,
            "timestamp": datetime.now()
        }

        self.dispenser.record_transaction(transaction)
        return transaction

    def dispense_fuel_by_amount(self, fuel_type, amount):
        fuel = self.dispenser.get_fuel(fuel_type)
        liters_dispensed, total_cost = fuel.dispense_by_amount(amount)

        transaction = {
            "attendant": self.full_name,
            "fuel": fuel_type,
            "liters": liters_dispensed,
            "total_cost": total_cost,
            "timestamp": datetime.now()
        }

        self.dispenser.record_transaction(transaction)
        return transaction