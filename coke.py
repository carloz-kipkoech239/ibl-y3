# Define accepted denominations
DENOMINATIONS = [1, 5, 10, 25]

# Initialize amount due and coins inserted
amount_due = 50
coins_inserted = 0

# Prompt the user for input until enough coins have been inserted
while coins_inserted < amount_due:
    # Prompt the user to insert a coin
    coin = int(input("Insert a coin : "))
    
    # Check if the coin is an accepted denomination
    if coin not in DENOMINATIONS:
        print("Invalid coin denomination, please insert an accepted denomination.")
        continue
    
    # Add the value of the coin to the amount inserted
    coins_inserted += coin
    
    # Calculate the new amount due
    amount_due = max(amount_due - coin, 0)
    
    # Inform the user of the current amount due
    print("Amount due:", amount_due, "cents")
    
# Calculate the change owed
change = coins_inserted - amount_due

# Output the change owed
print("Change owed:", change, "cents")
