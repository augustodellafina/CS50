# Empty grocery list arr that will receive the grocery's list items
grocery_list = {}

def main():
  try:
    while True: # Let's start the loop
      item = input().title() # This line catch and read user input and title-case it

      # Add the grocery's item to the list :)
      if item in grocery_list:
        grocery_list[item] += 1
      else:
        grocery_list[item] = 1

  except EOFError:
    pass # If the user pressed control-d, then we exit the loop :(

  # Let's sort the grocery list to show it in the alphabetic order
  sorted_grocery_list = sorted(grocery_list.items())

  for item, count in sorted_grocery_list:
    # Added a counter line prefix and show the list when exit the loop
    print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()