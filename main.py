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
        if address:
            good_chars = ""   # We'll build a new version of the address with refined characters
            for char in address:   # Go through each letter/number/symbol in what they typed
                if char.isalnum() or char.isspace() or char == "," or char == "." or char == "-" or char == "/":
                    good_chars = good_chars + char  # Add this good character to our 'good_chars'
            if good_chars:
                break  
            else:
                print("Your address needs to have at least one letter or number. Try again.")
        else:
            print("You can't leave the address empty. Please type it in again.")

    while True:    # Loop until valid input is received
        phone = input("Enter phone number: ").strip()
        phone_without_spaces = phone.replace(" ", "")  # removes spaces from the phone number
        if not phone:  # Check if phone number is not empty
            print("Phone number cannot be empty. Please try again.")
            continue
        if not phone_without_spaces.isdigit() or '+' in phone_without_spaces:  # Check if phone number contains only digits
            print("Phone number must contain only digits (0 to 9) and cannot contain '+' or other characters. Please try again.")
            continue
        if len(phone_without_spaces) < 10 or len(phone_without_spaces) > 15:   # Check if phone number is between 10 and 15 digits
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
    """Get an order item with input validation."""
    while True:
        category = input("Enter quesadilla type (Regular/Gourmet, or 'done' to finish): ").title().strip()
        if category.lower() == "done":
            return None, None, 0  # Returns 0 to indicate end of order, None for item name and None for price
        found_item_1 = None
        for item in menu:
            if item[0] == category:
                found_item_1 = item
                break
        if not found_item_1:
            print("Invalid category. Please enter 'Regular' or 'Gourmet'.")
            continue
        item_name = input("Enter quesadilla name: ").title().strip()

        found_item_2 = None
        for item in menu:
            if item[1] == item_name:
                found_item_2 = item
                break

        if not found_item_2:
            print("Invalid item. Please enter a valid quesadilla name.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0 or quantity > 50:   # Check if quantity is a positive integer and not more than 50
                print("Quantity must be greater than zero and not more than 50.")
                continue
            return found_item_1[1], found_item_2[2], quantity

        except ValueError:
            print("Invalid quantity. Please enter a number.")


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
        print(f"- {item}: NZ${price:.2f}")   ## Print each item in the order with its price rounded to 2 decimal places

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
    filename = f"order_{customer_name.replace(' ', '_')}_{timestamp}.txt"   # Create a filename with the customer's name and timestamp
    try:
        filename = filename.replace("/", "_")  # Replace any '/' in the filename with '_'
    except Exception as e:
        print(f"Error creating filename: {e}")
    try:
        with open(filename, "w") as f:
            f.write("--- Queenstown Quesadillas Order ---\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z%z')}\n")   # Write the current date and time to the file also took a little help from YT
            f.write(f"Customer Name: {customer_name}\n")  
            if delivery_option == "D":
                f.write(f"Delivery Address: {address}\n")
                f.write(f"Phone Number: {phone}\n")
                f.write("Delivery Option: Delivery\n")
            else:
                f.write("Delivery Option: Pick-up\n")   # Delivery option
            f.write(f"Delivery Charge: ${5.00:.2f}\n")
            f.write("\n--- Items Ordered ---\n")
            for item, price in order:
                f.write(f"- {item}: ${price:.2f}\n")
            f.write(f"\nTotal Cost: ${total_cost:.2f} NZD\n")
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
