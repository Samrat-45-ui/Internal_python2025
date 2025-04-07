"""Quesadilla Ordering System. This program allows customers to order quesadillas with options for delivery or pick-up."""
# This program allows customers to order quesadillas with options for delivery or pick-up.

import datetime


def get_customer_name():
    """Get the customer's name with input validation."""
    while True:
        name = input("Enter your full name: ").strip()  # removes any of the extra spaces from the name
        name_without_spaces = name.replace(" ", "")  # removes spaces from the name
        if name_without_spaces and name_without_spaces.isalpha():   # checks if the name is not empty and contains only letters
            return name
        else:
            print("Name cannot be empty and must contain only letters. Please try again.")


def get_delivery_option():
    """Get the delivery option (D/P) with input validation."""
    while True:
        option = input("Delivery or Pick-up? (D/P): ").upper().strip()
        if option in ("D", "P"):
            return option
        else:
            print("Invalid option. Please enter 'D' or 'P'.")


def get_delivery_details():
    """Get delivery address and phone number with robust input validation."""
    while True:
        address = input("Enter your delivery address: ").strip()
        if address and all(char.isalnum() or char.isspace() or char in ",./'" for char in address) and len(address) > 10:   # checks if the address is not empty and contains only letters, numbers, spaces, and some special characters
            break
        else:
            print("Invalid address. Please include only letters, numbers, spaces, and these special characters (, . /). Address must be longer than 10 characters. Try again.")
    while True:
        phone = input("Enter phone number: ").strip()
        phone_without_spaces = phone.replace(" ", "")
        if not phone:
            print("Phone number cannot be empty. Please try again.")
            continue
        if not phone_without_spaces.isdigit():
            print("Phone number must contain only digits (0 to 9). Please try again.")
            continue
        if len(phone_without_spaces) < 10 or len(phone_without_spaces) > 15:
            print("Phone number must be between 10 and 15 digits. Please try again.")
            continue
        break
    return address, phone


def display_menu(menu):
    """Display the menu."""
    print("\n--- Menu --- ")
    for item in menu:   # Loop through each item in the menu and print it out
        print(f"- {item[0]} - {item[1]}: ${item[2]:.2f}")


def get_order_item(menu):
    """Get an order item with validation."""
    while True:
        category = input("Enter quesadilla category (Regular/Gourmet, or 'done' to finish): ").title().strip()
        if category.lower() == "done":
            return None, None, 0   # Exit the loop if 'done' is entered
        item_name = input("Enter quesadilla name: ").strip()
        found_item = None
        for item in menu:
            if item[0].lower() == category.lower() and item[1].lower() == item_name.lower():
                found_item = item
                break
        if not found_item:
            print("Invalid category or quesadilla name.")
            continue

        quantity_str = input(f"Enter quantity for {item_name}: ")
        try:
            quantity = int(quantity_str)
            if quantity <= 0:
                print("Quantity must be a positive integer. Please try again.")
            else:
                return found_item[1], found_item[2], quantity  # Exit the loop if a valid quantity is entered
        except ValueError:
            print("Invalid input. Please enter a whole number for the quantity. Please try again.")


def display_order_summary(customer_name, order, total_cost, delivery_option, address, phone, delivery_charge):
    """Display the order summary."""
    print("\n--- Order Summary ---")
    print(f"Customer Name: {customer_name}")

    if delivery_option == "D":
        if not address or not phone:
            print("Error: Missing delivery details. Please ensure address and phone number are provided.")
            return
        print(f"Delivery Address: {address}")
        print(f"Phone Number: {phone}")
        total_cost += delivery_charge
        print(f"Delivery Charge: ${delivery_charge:.2f}")

    if not order:
        print("Error: No items in the order. Please add items to the order.")
        return

    print("\n--- Items Ordered ---")
    for item, price in order:
        print(f"- {item}: NZ${price:.2f}")   # Print each item in the order with its price rounded to 2 decimal places

    print(f"\nTotal Cost: NZ${total_cost:.2f}")


def process_order(menu):
    """Process the order, handling item selection and quantity."""
    order = []
    total_cost = 0.0
    while True:
        item_details = get_order_item(menu)
        if item_details[0] is None:
            break  # End of order

        item_name, price, quantity = item_details
        order.extend([(item_name, price)] * quantity)   # Adds the item to the order list for the specified quantity
        total_cost += price * quantity
    return order, total_cost


def confirm_order():
    """Confirm the order with the customer."""
    while True:
        confirm = input("\nConfirm order? (Y/N): ").upper().strip()
        if confirm == "Y" or "Yes" in confirm:
            return True
        elif confirm == "N" or "No" in confirm:
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def export_order_details(customer_name, order, total_cost, delivery_option, address, phone):
    """Export the order details to a file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # Format the timestamp
    filename = f"order_{customer_name.replace(' ', '_')}_{timestamp}.txt"   # Creates a filename with the customer's name and timestamp
    try:
        filename = filename.replace("/", "_")  # Replace any '/' in the filename with '_'
    except Exception as e:
        print(f"Error creating filename: {e}")
    try:
        with open(filename, "w") as f:
            f.write("--- Queenstown Quesadillas Order ---\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z%z')}\n")   # Writes the current date and time to the file also took a little help from YT
            f.write(f"Customer Name: {customer_name}\n")   # Writes the customer's name to the file
            if delivery_option == "D":
                f.write(f"Delivery Address: {address}\n")
                f.write(f"Phone Number: {phone}\n")
                f.write("Delivery Option: Delivery\n")
                f.write(f"Delivery Charge: NZ${5.00:.2f}\n")
            else:
                f.write("Delivery Option: Pick-up\n")   # Delivery option
            f.write("\n--- Items Ordered ---\n")
            for item, price in order:
                f.write(f"- {item}: NZ${price:.2f}\n")
            f.write(f"\n--- Total Cost: NZ${total_cost:.2f} ---\n")
        print(f"\nOrder details exported to '{filename}'")
    except Exception as e:
        print(f"Error exporting order details: {e}")


def main():
    """Handle the order processing and interconnect the overall system."""
    menu = [
        ["Regular", "Cheese Quesadilla", 8.50],
        ["Regular", "Chicken Quesadilla", 10.00],
        ["Regular", "Beef Quesadilla", 11.00],
        ["Regular", "Vegetable Quesadilla", 9.50],
        ["Gourmet", "Shrimp Quesadilla", 13.00],
        ["Gourmet", "Pulled Pork Quesadilla", 12.50],
        ["Gourmet", "Spicy Chorizo Quesadilla", 12.00],
        ["Gourmet", "Mushroom and Truffle Quesadilla", 14.00],
        ["Gourmet", "Vegetarian Quesadilla", 11.00],
    ]

    delivery_charge = 5.00

    while True:
        print("\n--- Welcome to Queenstown Quesadillas ---")  # Welcome message..
        print("Please enter your details to place an order.")  # Prompt for customer details...
        print("Note: Delivery incurs a charge of $5.00.")
        customer_name = get_customer_name()  # Get the customer's name
        delivery_option = get_delivery_option()

        address, phone = None, None
        if delivery_option == "D":
            address, phone = get_delivery_details()
        display_menu(menu)  # Display the menu

        print("\n--- New Order ---")  # Indicate the start of a new order
        order, total_cost = process_order(menu)  # Get the order

        if not order:
            print("No items were added to the order.")

        display_order_summary(customer_name, order, total_cost, delivery_option, address, phone, delivery_charge)
        if order:  # Only ask to confirm if there was an order made
            print("Please confirm your order:")
            if confirm_order():
                print("Order confirmed!")
                export_order_details(customer_name, order, total_cost, delivery_option, address, phone)  # Export the details
            else:
                print("Order cancelled.")

        if input("\nStart a new/ next order? (Y/N): ").upper().strip() != "Y":
            print("Thank you for the order!")
            break


main()
