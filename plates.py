def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def starts_with_letters(s):
    if len(s) < 2:
        return False
    first_two = s[:2]
    return first_two.isalpha()

def has_valid_numbers(s):
    if not s[0].isalpha():
        return False  # Check if the first character is a letter
    first_digit = None
    for i, char in enumerate(s):
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            if first_digit == '0':
                return False  # The first number is '0', which is invalid
        elif first_digit is not None:
            break  # We found a non-digit character after the first number
    return True

def has_valid_length(s):
    return 2 <= len(s) <= 6

def has_no_punctuation(s):
    return all(char.isalnum() for char in s)

def is_valid(s):
    return starts_with_letters(s) and has_valid_numbers(s) and has_valid_length(s) and has_no_punctuation(s)

main()
