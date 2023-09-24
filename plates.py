# Function to handle the main logic of the program
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to check if the vanity plate starts with at least two letters
def starts_with_letters(s):
    if len(s) < 2:
        return False
    first_two = s[:2]
    return first_two.isalpha()

# Function to check if the vanity plate has valid numbers at the end
def has_valid_numbers(s):
    if not s[:1].isalpha():
        return False  # Check if the two first characters is a letter
    first_digit = None
    for i, char in enumerate(s):
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            if first_digit == '0':
                return False  # The first number is '0', which is invalid
        elif first_digit is not None and i < len(s) - 1:
            return False  # We found a non-digit character after the first number but before the end
    return True

# Function to check if the vanity plate has a valid length (2 to 6 characters)
def has_valid_length(s):
    return 2 <= len(s) <= 6

# Function to check if the vanity plate has no punctuation marks
def has_no_punctuation(s):
    return all(char.isalnum() for char in s)

# Function to check if the vanity plate is valid based on all requirements
def is_valid(s):
    return starts_with_letters(s) and has_valid_numbers(s) and has_valid_length(s) and has_no_punctuation(s)

# Entry point of the program
main()
