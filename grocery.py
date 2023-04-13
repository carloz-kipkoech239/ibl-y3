# Initialize an empty dictionary to store the items and their counts
items = {}

# Prompt the user for input until they input control-d
while True:
    try:
        # Prompt the user to enter an item
        item = input("item: ")
        
        # Check if the user has entered control-d
        if not item:
            break
        
        # Convert the item to uppercase and add it to the dictionary
        item = item.upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
        
    except EOFError:
        # Exit the loop if control-d was entered
        break

# Sort the items alphabetically and output them with their counts
for item in sorted(items.keys()):
    count = items[item]
    print("{:2d} {}".format(count, item))
