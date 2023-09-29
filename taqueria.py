menu = ({
  "Baja Taco": 4.00,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
})


def main():
  total_cost = 0.0

  try:
    while True:
      item = input("Item: ").title() # This line catch and read user input and title-case it

      # Check if the user input is a valid item from the menu
      if item in menu:
        total_cost += menu[item] # Add the item's price to the total
      else:
        print("Invalid Item, Please choose something from the Menu.")
      
      # Now let's display the current total cost
      print(f"Total: ${total_cost:.2f}")

  except EOFError:
    pass # If the user pressed control-d, then we exit the loop

  print("Thank you for your order!")

if __name__ == "__main__":
    main()