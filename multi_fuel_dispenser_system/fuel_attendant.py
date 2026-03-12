from datetime import datetime

from multi_fuel_dispenser_system.dispenser import Dispenser
from multi_fuel_dispenser_system.fuel import Fuel


class FuelAttendant:
    def __init__(self, full_name: str, dispenser: Dispenser):
        if not full_name.strip():
            raise ValueError("Attendant name cannot be empty.")
        self.full_name = full_name
        self.dispenser = dispenser
        self.transactions = []

    def add_new_fuel(self, fuel_type: str, price_per_liter: float, quantity: float):
        fuel = Fuel(fuel_type, price_per_liter, quantity)
        self.dispenser.add_fuel(fuel)

    def get_available_fuels(self):
        return self.dispenser.get_available_fuels()

    def update_fuel_price(self, fuel_type: str, new_price: float):
        fuel = self.dispenser.get_fuel(fuel_type)
        fuel.update_price(new_price)

    def restock_fuel(self, fuel_type: str, quantity: float):
        fuel = self.dispenser.get_fuel(fuel_type)
        fuel.restock(quantity)

    def dispense_by_liters(self, fuel_type: str, liters: float):
        if liters <= 0 or liters > 50:
            raise ValueError("Liters must be between 1 and 50.")
        fuel = self.dispenser.get_fuel(fuel_type)
        fuel.reduce_quantity(liters)
        total_cost = liters * fuel.price_per_liter

        return self._record_transaction(fuel_type, liters, total_cost)

    def dispense_by_amount(self, fuel_type: str, amount: float):
        fuel = self.dispenser.get_fuel(fuel_type)
        if amount <= fuel.price_per_liter:
            raise ValueError("Amount must be greater than price of one liter.")
        liters = amount / fuel.price_per_liter

        if liters > 50:
            raise ValueError("Cannot dispense more than 50 liters at once.")
        fuel.reduce_quantity(liters)

        return self._record_transaction(fuel_type, liters, amount)

    def _record_transaction(self, fuel_type, liters, amount):
        transaction = {
            "attendant": self.full_name,
            "fuel": fuel_type,
            "liters": round(liters, 2),
            "amount": round(amount, 2),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.transactions.append(transaction)
        return transaction

    def show_transactions(self):
        return self.transactions