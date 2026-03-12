from multi_fuel_dispenser_system.fuel import Fuel


class Dispenser:
    def __init__(self):
        self.fuels = {}

    def add_fuel(self, fuel: Fuel):
        if fuel.fuel_type in self.fuels:
            raise ValueError("Fuel already exists.")
        self.fuels[fuel.fuel_type] = fuel

    def get_fuel(self, fuel_type: str):
        if fuel_type not in self.fuels:
            raise ValueError("Fuel type not found.")
        return self.fuels[fuel_type]

    def get_available_fuels(self):
        return {
            name: {
                "price_per_liter": fuel.price_per_liter,
                "quantity": fuel.quantity,
            }
            for name, fuel in self.fuels.items()
        }