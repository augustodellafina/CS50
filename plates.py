def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def starts_with_letters(s):
    # Check if the first two characters are letters
    return s[:2].isalpha()

def has_valid_length(s):
    # Check if the length of the string is between 2 and 6 characters
    return 2 <= len(s) <= 6

def no_invalid_numbers(s):
    # Check if the first character is not '0', and there are no numbers in the middle
    return s[0] != '0' and all(char.isalpha() for char in s[2:-1])

def has_numbers_at_end(s):
    # Check if the last character is a number
    return s[-1].isdigit()

def is_valid(s):
    # Check all the requirements
    return starts_with_letters(s) and has_valid_length(s) and no_invalid_numbers(s) and has_numbers_at_end(s)

main()
