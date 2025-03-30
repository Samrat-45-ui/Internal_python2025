def quesadillas():
    """Handle quesadilla orders."""
    menu = [
        ["Regular", "Cheese Quesadilla", 8.50],
        ["Regular", "Chicken Quesadilla", 10.00],
        ["Regular", "Beef Quesadilla", 11.00],
        ["Regular", "Vegetable Quesadilla", 9.50],
        ["Gourmet", "Shrimp Quesadilla", 13.00],
        ["Gourmet", "Pulled Pork Quesadilla", 12.50],
        ["Gourmet", "Spicy Chorizo Quesadilla", 12.00],
        ["Gourmet", "Mushroom and Truffle Quesadilla", 14.00],
    ]

    delivery_charge = 5.00

def get_customer_name():
    """Get the customer's name with input validation."""
    while True:
        name = input("Enter customer name: ").strip()  # removes any of the extra spaces from the name
        if name and name.isalpha():   # checks if the name is not empty
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
    """Get delivery address and phone number with input validation."""
    address = input("Enter delivery address: ").strip()
    if address == "":
        print("Address cannot be empty.")
        return get_delivery_details()
    phone = input("Enter phone number: ").strip()
    if phone == "":
        print("Phone number cannot be empty.")
        return get_delivery_details() 
    return address, phone


def display_menu(menu):
    """Display the menu."""
    print("\n--- Menu ---")
    for item in menu:
        print(f"- {item[0]} - {item[1]}: ${item[2]:.2f}")

def get_order_item(menu):
    """Get an order item with input validation."""
    while True:
        category = input("Enter quesadilla type (Regular/Gourmet, or 'done' to finish): ").title().strip()
        if category.lower() == "done":
            return None, None, 0 #Returning 0 to indicate end of order, None for item name and None for price

        item_name = input("Enter quesadilla name: ").title().strip()

        found_item = None
        for item in menu:
            if item[0] == category and item[1] == item_name:
                found_item = item
                break

        if not found_item:
            print("Invalid category or quesadilla name.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            return found_item[1], found_item[2], quantity

        except ValueError:
            print("Invalid quantity. Please enter a number.")