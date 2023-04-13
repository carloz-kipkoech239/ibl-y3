# Initialize fuel level to 0%
fuel_level = 0

# Prompt the user for input until a valid fraction is entered
while True:
    # Prompt the user to enter a fraction
    fraction = input("fuel capacity: ")
    
    try:
        # Split the fraction into X and Y
        x, y = map(int, fraction.split("/"))
        
        # Check for invalid input
        if x > y or y == 0:
            raise ValueError
        
        # Calculate the fuel level
        fuel_level = x / y * 100
        
        # Round the fuel level to the nearest integer
        fuel_level = round(fuel_level)
        
        # Check for full or empty tank
        if fuel_level >= 99:
            fuel_level = "F"
        elif fuel_level <= 1:
            fuel_level = "E"
        
        # Exit the loop if a valid fraction was entered
        break
    
    except (ValueError, ZeroDivisionError):
        # Prompt the user again if invalid input was entered
        print("Invalid input, please enter a valid fraction.")
        
# Output the fuel level
print("Fuel level:", fuel_level, "%")
