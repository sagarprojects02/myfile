# Name: P Sagar Yadav
# Project: Personal Information Display Program
# Description: This program stores and displays personal information
# using variables, user input, string formatting, and basic validation.

print("=" * 50)
print("        WELCOME TO MY PERSONAL INFO PROGRAM")
print("=" * 50)

# Static personal information
name = "P Sagar Yadav"     # String variable to store name
age = 23                   # Integer variable to store age
city = "Tirupati"         # String variable to store city
hobby = "Playing PUBG"           # String variable to store hobby

# Get favorite food from user
favorite_food = input("Enter your favorite food: ").strip()

while favorite_food == "":
    print("Favorite food cannot be empty. Please enter again.")
    favorite_food = input("Enter your favorite food: ").strip()

# Get favorite color from user
favorite_color = input("Enter your favorite color: ").strip()

while favorite_color == "":
    print("Favorite color cannot be empty. Please enter again.")
    favorite_color = input("Enter your favorite color: ").strip()

# Calculate age in months
age_in_months = age * 12

# Display formatted personal information
print("\n" + "=" * 50)
print("              PERSONAL INFORMATION")
print("=" * 50)

print(f"Name           : {name.title()}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.capitalize()}")

print("\n" + "-" * 50)
print("              USER PREFERENCES")
print("-" * 50)

print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.capitalize()}")

print("=" * 50)

print("\nThank you for using the Personal Info Program!")
print("Have a great day! 😊")
print("=" * 50)

