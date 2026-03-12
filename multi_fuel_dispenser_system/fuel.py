class Fuel:
    def __init__(self, fuel_type: str, price_per_liter: float, quantity: float):

        self._validate_fuel_type(fuel_type)
        self.fuel_type = fuel_type

        self._validate_price(price_per_liter)
        self.price_per_liter = price_per_liter

        self._validate_quantity(quantity)
        self.quantity = quantity

    def update_price(self, new_price: float):
        self._validate_price(new_price)
        self.price_per_liter = new_price

    def restock(self, amount: float):
        self._validate_amount(amount)
        self.quantity += amount

    def reduce_quantity(self, amount: float):
        self._validate_amount(amount)

        if amount > self.quantity:
            raise ValueError("Insufficient fuel in stock.")
        self.quantity -= amount

    def _validate_fuel_type(self, fuel_type: str):
        if not fuel_type.strip():
            raise ValueError("Fuel type cannot be empty.")

    def _validate_price(self, price: float):
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

    def _validate_quantity(self, quantity: float):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
