# Prompt the user for input
text = input("Input: ")

# Create a string to store the result with vowels removed
result = ""

# Iterate through each character in the input text
for char in text:
    # Check if the character is a vowel (both uppercase and lowercase)
    if char.lower() not in 'aeiou':
        result += char

# Print the result
print(f"Output: {result}")
