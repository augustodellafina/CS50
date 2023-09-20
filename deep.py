# deep.py

# Prompt the user for input
user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Check if the input is equal to "42" (case-insensitive) or "forty-two" (case-insensitive)
if user_input.lower() == "42" or user_input.lower() == "forty-two" or user_input.lower() == "forty two":
    print("Yes")
else:
    print("No")
