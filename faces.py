# faces.py

# Define the convert function
def convert(input_str):
    # Replace :) with 🙂 and :( with 🙁
    modified_str = input_str.replace(":)", "🙂").replace(":(", "🙁")
    return modified_str

# Define the main function
def main():
    # Prompt the user for input
    user_input = input("How are you felling: ")
    
    # Call the convert function and print the result
    converted_input = convert(user_input)
    print(converted_input)

# Call the main function
if __name__ == "__main__":
    main()
