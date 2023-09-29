grocery_list = {}

def main():
  try:
    while True:
      item = input("Add item: ").title()
      if item in grocery_list:
        grocery_list[item] += 1
      else:
        grocery_list[item] = 1
  except EOFError:
    pass
    print("\n")

  sorted_grocery_list = sorted(grocery_list.items())

  for item, count in sorted_grocery_list:
    print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()