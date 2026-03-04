from multi_fuel_dispenser_system.fuel import Fuel


class Dispenser:
    def __init__(self):
        self.fuels = {}
        self.transactions = []

    def add_fuel(self, fuel):
        self.fuels[fuel.fuel_type] = fuel

    def get_available_fuels(self):
        return {
            name: fuel.price_per_liter
            for name, fuel in self.fuels.items()
        }

    def get_fuel(self, fuel_type: str):
        if fuel_type not in self.fuels:
            raise ValueError("Fuel not found.")
        return self.fuels[fuel_type]

    def record_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions
