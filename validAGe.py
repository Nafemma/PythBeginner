age = 0
while age <= 0:
    age =  int(input("Please enter your age: "))
    if age <= 0:
        print("Please enter a valid age.")
print(f"You are {age} years old.")