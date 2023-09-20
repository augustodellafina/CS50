# interpreter.py

# Prompt the user for an arithmetic expression
expression = input("Enter an arithmetic expression (x + y, x - y, x * y, x / y): ")

# Split the expression into its components
x, operator, y = expression.split()

# Convert the values to integers
x = int(x)
y = int(y)

# Calculate the result based on the operator
if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

# Format and output the result as a floating-point value with one decimal place
print("{:.1f}".format(result))
