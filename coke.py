# Initialize variables to keep track of the total amount and accepted coin denominations
total_amount = 0
amount_due = 50
accepted_coins = [25, 10, 5]

# Continue looping until the total amount reaches 50 cents or more
while total_amount < 50:
    try:
        # Prompt the user for a coin input and convert it to an integer
        coin = int(input("Insert Coin: "))
        
        # Check if the coin is an accepted denomination
        if coin in accepted_coins:
            amount_due -= coin
            total_amount += coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {amount_due}")
            print("Invalid coin. Please insert a 25, 10, or 5 cent coin.")
    except ValueError:
        print(f"Amount Due: {amount_due}")
        print("Invalid input. Please enter a valid integer.")

# Calculate and display the change owed
change_owed = total_amount - 50
if change_owed > 0:
    print(f"Change Owed: {change_owed}")
