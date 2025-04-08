# <---------------------------------------------------->
#the and operator
#the and operator is used to combine two or more conditions
#it returns True if all the conditions are true
#it returns False if any of the conditions are false
#example
username = "Albelle"
password = "1234"

login = input("Enter your username: ")
login2 = input("Enter your password: ")
if login == username and login2 == password:
    print(f"Welcome back {username}!")
else:
    print("username or password incorrect")