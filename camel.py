# Get the input in camel case from the user
camel_case = input("Enter a variable name in camel case: ")

# Initialize an empty string for the snake case version
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

# Print the snake case version of the variable name
print("camelCase: " + camel_case, end='\n'
      "snake_case: " + snake_case
)
