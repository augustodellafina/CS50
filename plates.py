def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Requirement 1: Plate must have at least 2 letters at the beginning
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Requirement 2: Plate must have a maximum of 6 characters
    if len(s) > 6:
        return False

    # Requirement 3: Numbers cannot be in the middle, and the first number cannot be 0
    if s[2:].isdigit():
        if s[2] == '0':
            return False
        if not s[2:].isnumeric():
            return False

    # Requirement 4: No periods, spaces, or punctuation marks are allowed
    if any(char in ". ,;:!?" for char in s):
        return False

    # If all requirements are met, return True
    return True

main()
