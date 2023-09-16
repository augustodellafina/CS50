# einstein.py

# Prompt the user for mass as an integer (in kilograms)
mass_str = input("Enter mass in kilograms: ")

# Convert the input mass string to an integer
mass = int(mass_str)

# Speed of light in meters per second
speed_of_light = 300000000  # meters per second

# Calculate the energy using E=mc^2
energy = mass * speed_of_light ** 2

# Print the equivalent energy as an integer
print("Equivalent energy (Joules):", energy)
