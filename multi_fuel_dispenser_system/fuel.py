class Fuel:
    def __init__(self, fuel_type, price_per_liter, quantity):

        self.fuel_type = fuel_type

        self.__validate_price()
        self.price_per_liter = price_per_liter

        self.__validate_quantity()
        self.quantity = quantity


    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("New price must be greater than zero.")
        self.price_per_liter = new_price


    def restock(self, additional_quantity):
        if additional_quantity <= 0:
            raise ValueError("Restock quantity must be greater than zero.")
        self.quantity += additional_quantity


    def dispense_by_liters(self, liters):
        if liters <= 0 or liters > 50:
            raise ValueError("Liters must be between 1 and 50.")
        if liters > self.quantity:
            raise ValueError("Insufficient fuel in stock.")

        total_cost = liters * self.price_per_liter
        self.quantity -= liters
        return liters, total_cost


    def dispense_by_amount(self, amount):
        if amount <= self.price_per_liter:
            raise ValueError("Amount must be greater than price of one liter.")

        liters = amount / self.price_per_liter

        if liters > self.quantity:
            raise ValueError("Insufficient fuel in stock.")

        self.quantity -= liters
        return liters, amount

    def __validate_price(self):
        if self.price_per_liter <= 0:
            raise ValueError("Price must be greater than zero.")

    def __validate_quantity(self):
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")