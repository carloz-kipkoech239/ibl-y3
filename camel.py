# Prompt the user for input
camel_case_name = input("what is your name?: ")

# Convert camel case to snake case
snake_case_name = ""
for i, char in enumerate(camel_case_name):
    if char.isupper() and i != 0:
        snake_case_name += "_"
    snake_case_name += char.lower()

# Output the snake case name
print("Snake case name:", snake_case_name)
