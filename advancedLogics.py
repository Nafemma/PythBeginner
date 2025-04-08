#the or operator
#the or operator is used to combine two or more conditions
#it returns True if any of the conditions is true
#it returns False if all the conditions are false
#example

cardType = input(str("enter your card type: "))
if (cardType.lower() == "Passport" or cardType.lower() == "National ID") or cardType.lower() == "License":
    print("you can proceed")
else:
    print("you cannot proceed")