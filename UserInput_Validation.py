#user input validation
#keep asking for input until user enters a valid respoonse
#age Retry system

age = -1
while age <= 0:
    age = int(input('Enter your age: '))
    if age <= 0:
        print('invalid input, please try again!')
print(f"you are {age} years old")    
        