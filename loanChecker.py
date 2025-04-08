creditScore = 6
income = 70000
employmentStatus = "employed"
loanAmount = 10000

if (employmentStatus == "employed" or employmentStatus == "self-employed") and income > 50000 and creditScore > 5:
    if loanAmount < 20000:
        print("Loan approved")
    else:
        print("Loan amount too high")