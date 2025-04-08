# User Profile Generator
#an assignment to create a user profile generator that takes input and stores in a dictionary

# b requirements
# accepting user Input
fullName = input("Enter your full name: ")
age = int(input("Enter your age: "))
heightInMeters = float(input("Enter your height in meters: "))
favoriteLanguage = input("Enter your favorite programming language: ")
hobbies = input("Enter your hobbies (comma-separated, e.g., 'reading, coding, hiking'): ")

#c Store Data
#using a dicitonary to store data
user_profile = {
    "fullName": fullName,
    "age": age,
    "heightInMeters": heightInMeters,
    "favoriteLanguage": favoriteLanguage,
    "hobbies": hobbies
}

# d Perform Operations on data
# Calculate birth year (assuming current year is 2025)
currentYear = 2025
birthYear = currentYear - age
user_profile["birthYear"] = birthYear

# Convert height to centimeters
heightInCentimeters = heightInMeters * 100
user_profile["heightInCentimeters"] = heightInCentimeters

# Count number of hobbies
hobbiesList = hobbies.split(",")
numOfHobbies = len(hobbiesList)
user_profile["numOfHobbies"] = numOfHobbies

# Check if user loves Python (case-insensitive)
isPythonLover = favoriteLanguage.lower() == "python"
user_profile["is_favorite_python"] = isPythonLover

# Format full name to ensure proper capitalization
formatted_name = " ".join([name.capitalize() for name in fullName.split()])
user_profile["formatted_name"] = formatted_name

# Format hobbies list
formatted_hobbies = [hobby.strip().capitalize() for hobby in hobbiesList]
user_profile["formatted_hobbies"] = formatted_hobbies

# Output
print("\nUser profile summary:")
print(f"Full Name: {formatted_name}")
print(f"Age: {age} years")
print(f"Birth Year: {birthYear}")
print(f"Height: {heightInMeters:.2f} meters ({heightInCentimeters:.2f} centimeters)")
print(f"Favorite Programming Language: {favoriteLanguage}")
print(f"Is Favorite Language Python? {'Yes' if isPythonLover else 'No'}")
print(f"Number of Hobbies: {numOfHobbies}")
print(f"Hobbies: {', '.join(formatted_hobbies)}")

# Print the user_profile dictionary
print("\nUser Profile Dictionary:")
print(user_profile)