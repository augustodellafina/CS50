def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Requirement 1: Plate must start with at least two letters
    if len(s) < 2:
        return False

    # Requirement 2: Plate must contain between 2 and 6 characters (letters or numbers)
    if len(s) < 2 or len(s) > 6:
        return False

    # Requirement 3: Numbers cannot be used in the middle of the plate
    if not s[-1].isnumeric() or s[0] == '0':
        return False

    # Requirement 4: No periods, spaces, or punctuation marks are allowed
    if any(not char.isalnum() for char in s):
        return False

    # Requirement 5: Numbers must come at the end
    if any(char.isnumeric() for char in s[:-1]):
        return False

    # If all requirements are met, the plate is valid
    return True

main()