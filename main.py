from multi_fuel_dispenser_system.dispenser import Dispenser
from multi_fuel_dispenser_system.fuel_attendant import FuelAttendant


def print_menu():
    print("\n====== MFDS MENU ======")
    print("1. Add New Fuel")
    print("2. View Available Fuels")
    print("3. Update Fuel Price")
    print("4. Restock Fuel")
    print("5. Dispense Fuel by Liters")
    print("6. Dispense Fuel by Amount")
    print("7. Show Transactions")
    print("8. Exit")
    print("=======================")


def main():

    dispenser = Dispenser()
    attendant_name = input("Enter Attendant Name: ")

    attendant = FuelAttendant(attendant_name, dispenser)

    while True:

        print_menu()
        choice = input("Choose an option: ")

        try:

            if choice == "1":
                fuel_type = input("Enter Fuel Type: ")
                price = float(input("Enter Price per liter: "))
                quantity = float(input("Enter quantity: "))

                attendant.add_new_fuel(fuel_type, price, quantity)
                print("Fuel added successfully.")

            elif choice == "2":
                fuels = attendant.get_available_fuels()

                if not fuels:
                    print("No fuels available.")
                else:
                    for name, details in fuels.items():
                        print(
                            f"{name} | Price: ₦{details['price_per_liter']} | Quantity: {details['quantity']}L"
                        )

            elif choice == "3":
                fuel_type = input("Enter Fuel Type: ")
                new_price = float(input("Enter new price: "))

                attendant.update_fuel_price(fuel_type, new_price)
                print("Fuel price updated.")

            elif choice == "4":
                fuel_type = input("Enter Fuel Type: ")
                quantity = float(input("Enter Quantity to add: "))

                attendant.restock_fuel(fuel_type, quantity)
                print("Fuel restocked successfully.")

            elif choice == "5":
                fuel_type = input("Enter Fuel Type: ")
                liters = float(input("Enter the Liters to buy: "))

                transaction = attendant.dispense_by_liters(fuel_type, liters)

                print("\nTransaction Successful")
                print(transaction)

            elif choice == "6":
                fuel_type = input("Enter Fuel Type: ")
                amount = float(input("Enter the Amount to buy: "))

                transaction = attendant.dispense_by_amount(fuel_type, amount)

                print("\nTransaction Successful")
                print(transaction)

            elif choice == "7":
                transactions = attendant.show_transactions()

                if not transactions:
                    print("No transactions yet.")
                else:
                    for list_of_transactions in transactions:
                        print(list_of_transactions)

            elif choice == "8":
                print("Exiting...")
                break

            else:
                print("Invalid choice, try again...")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()