def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Requirement 1: Vanity plates must start with at least two letters.
    if len(s) < 2:
        return False

    # Requirement 2: Vanity plates may contain a maximum of 6 characters
    # (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # Requirement 3: Numbers cannot be used in the middle of a plate (between letters);
    # they must come at the end. The first number used cannot be a '0'.
    has_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            if i == 0:
                if s[i] == '0':
                    return False
                has_number = True
            else:
                if has_number:
                    return False
        elif has_number and not s[i].isalpha():
            return False

    # Requirement 4: No periods, spaces, or punctuation marks are allowed.
    if any(char in '. ,;:!?-' for char in s):
        return False

    return True

main()
