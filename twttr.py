# Prompt the user for input
text = input("Enter text: ")

# Remove vowels from the text
text_without_vowels = ""
for char in text:
    if char.lower() not in "aeiou":
        text_without_vowels += char

# Output the text without vowels
print("Text without vowels:", text_without_vowels)
