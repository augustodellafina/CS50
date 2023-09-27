def main():
    while True:
        try:
            fraction = input("Enter a fraction (X/Y): ").strip()
            x, y = map(int, fraction.split('/'))
            
            if y == 0 or x > y or x < 0:
                raise ValueError
            
            percentage = (x / y) * 100
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            
            break  # Exit the loop if the input is valid and processed.
        
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction (X/Y).")

main()