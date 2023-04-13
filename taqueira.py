# Define the menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the order total to 0
order_total = 0.0

# Prompt the user for input until they input control-d
while True:
    try:
        # Prompt the user to enter an item
        item = input("0rder!!: ")
        
        # Check if the user has entered control-d
        if not item:
            break
        
        # Look up the item in the menu and add its price to the order total
        item = item.title()
        if item in menu:
            order_total += menu[item]
        
        # Output the order total
        print("${:.2f}".format(order_total))
        
    except EOFError:
        # Exit the loop if control-d was entered
        break
