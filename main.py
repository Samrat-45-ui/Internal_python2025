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
        if name:   # checks if the name is not empty
            return name
        else:
            print("Name cannot be empty. Please try again.")

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
    phone = input("Enter phone number: ").strip()
    return address, phone