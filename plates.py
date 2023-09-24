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
    if s[-1] == '0':
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and not s[i + 1].isdigit():
            return False
    return True

def has_valid_length(s):
    return 2 <= len(s) <= 6

def has_no_punctuation(s):
    return all(char.isalnum() for char in s)

def is_valid(s):
    return starts_with_letters(s) and has_valid_numbers(s) and has_valid_length(s) and has_no_punctuation(s)

main()
