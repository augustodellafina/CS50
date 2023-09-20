# meal.py

def main():
    # Prompt the user for a time in 24-hour format
    time_input = input("Enter the time in 24-hour format (HH:MM): ")

    # Call the convert function to get the time in hours as a float
    time_in_hours = convert(time_input)

    # Determine meal time based on the provided time
    meal_time = get_meal_time(time_in_hours)

    # Output the meal time if it's mealtime
    if meal_time:
        print(meal_time)


def convert(time):
    # Split the time input into hours and minutes
    hours, minutes = time.split(":")
    
    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)
    
    # Calculate the time in hours as a float
    time_in_hours = hours + (minutes / 60)
    
    return time_in_hours


def get_meal_time(time_in_hours):
    # Define meal time ranges in hours
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    # Check if the provided time falls within any meal time range
    if breakfast_start <= time_in_hours <= breakfast_end:
        return "breakfast time"
    elif lunch_start <= time_in_hours <= lunch_end:
        return "lunch time"
    elif dinner_start <= time_in_hours <= dinner_end:
        return "dinner time"
    else:
        # It's not mealtime
        return None


if __name__ == "__main__":
    main()
