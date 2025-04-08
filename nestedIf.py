#nesting if conditions

gender = input("What is your gender? :")
hasId = True
if gender == gender.lower() == "female":
    print("You are eligible to enter the class.")
    if hasId == True:
        print("You have an ID.")
    else:
        print("You don't have an ID.")
else:
    print("You are not eligible to enter the class.")
