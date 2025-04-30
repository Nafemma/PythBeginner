grade = int(input("Enter your grade: "))

match grade:
    case 80:
      print("You got an A")
    case 70:
      print("You got a B")
    case 60:
     print("You got a C")
    case 50:
     print("You got a D")
    case _ if grade >= 0 and grade < 50:
        print("You have failed")
    case _:
        print("Invalid grade")
        