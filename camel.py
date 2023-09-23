# Get the input in camel case from the user
camel_case = input("Enter a camel case input: ")

# Initialize an empty string for the snake case
snake_case = ""

# Iterate through each character in the camel case input
for char in camel_case:
    # Check if the character is uppercase
    if char.isupper():
        # Add an underscore before the uppercase character
        snake_case += "_"
        # Convert the uppercase character to lowercase and add it to the snake_case string
        snake_case += char.lower()
    else:
        # If the character is not uppercase, simply add it to the snake_case string
        snake_case += char

# Print the snake and camel case vesrions of the input
print("camelCase: " + camel_case, end='\n'
      "snake_case: " + snake_case
)
