import sys
import random

# Define a dictionary of available fonts
fonts = {
    "Arial": "Arial",
    "Helvetica": "Helvetica",
    "Times New Roman": "Times New Roman",
    "Courier": "Courier",
    "Verdana": "Verdana"
}

# Determine the font to use based on the command-line arguments
if len(sys.argv) == 1:
    # If there are no arguments, choose a random font
    font = random.choice(list(fonts.values()))
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font") and sys.argv[2] in fonts:
    # If there are two arguments and the first is -f or --font and the second is a valid font name, use the specified font
    font = fonts[sys.argv[2]]
else:
    # If the arguments are invalid, print an error message and exit
    print("Error: Invalid arguments")
    sys.exit(1)

# Prompt the user for text and output it in the chosen font
text = input("Enter some text: ")
print(f'<span style="font-family: {font};">{text}</span>')
