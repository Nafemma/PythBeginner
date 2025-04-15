#a password retry program using a while loop
# This program prompts the user to enter a password and allows a maximum of 3 attempts.

maxAttempt = 3
attempt = 0
storedPassword = "secret123"
while attempt < maxAttempt:
    password = input("Enter your password: ")
    if password == storedPassword: 
        print ("Access granted!")
        break
    else:
        attempt += 1
        print(f"Incorrect password! You have {maxAttempt - attempt} attempts left.")
else:
    print("Account Blocked! Too many failed attempts.")