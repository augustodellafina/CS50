def main():
    # Define a dictionary with fruits and their calorie values
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
    }

    # Prompt the user for input and convert it to lowercase for case-insensitive matching
    user_input = input("Enter a fruit: ").lower()

    # Check if the entered fruit is in the dictionary
    if user_input in fruit_calories:
        # Output the calorie value for the entered fruit
        print("Calories:", fruit_calories[user_input])
    else:
        print("Fruit not found")

main()