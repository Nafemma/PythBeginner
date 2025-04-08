#Notes: use of different variable names than the ones in the assignment 
# e.g currentAccount instead of current_account, accountNumber instead of account_number, etc. 
# due to preference of camelCase which is more readable for me. 
 
 
#Phase 1: Setup the Bank Database
#Create an accounts dictionary  
#Use account numbers as keys (e.g., 1001)

accounts = {
    1001: {
        'pin': '1234',
        'name': 'Nathan Banda',
        'balance': 150000.00
    },
    1002: {
        'pin': '5678',
        'name': 'Jane Nasibeko',
        'balance': 250000.50
    },
    1003: {
        'pin': '9012',
        'name': 'Chikondi Mbale',
        'balance': 800000.75
    }
}

currentAccount = None  # Tracks which account is logged in

#Phase 2: Build the Login System  
#Create an infinite loop (while True):  
while True:
    print("\nWelcome to the Bank ATM System")
    
    try:
        accountNumber = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        
        #Check if the account number exists in the accounts dictionary
        if accountNumber in accounts and accounts[accountNumber]['pin'] == pin:
            currentAccount = accountNumber
            print(f"Welcome, {accounts[currentAccount]['name']}!")
            break
        
        else:
            print("Invalid account number or PIN. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid account number and PIN.")
        
#Phase 3: Design the Main Menu  
#Create another infinite loop (runs while current_account exists):  
while currentAccount:
    print("\nMain Menu:")
    print("1. Check Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Money")
    print("4. Logout")
    
    try:
        choice = int(input("Please select an option (1-4): "))
        
        if choice == 1: #checking balance
            print(f"Your current balance is: MK{accounts[currentAccount]['balance']:.2f}")
            
        elif choice == 2: #withdraw cash
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Please enter a positive amount.")
                elif amount > accounts[currentAccount]['balance']:
                    print("Insufficient funds.")
                else:
                    accounts[currentAccount]['balance'] -= amount
                    print(f"Withdrawal successful! Your new balance is: MK{accounts[currentAccount]['balance']:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        
        elif choice == 3: #deposit money
            try:
                amount = float(input("Enter amount to deposit: MK"))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    accounts[currentAccount]['balance'] += amount
                    print(f"Deposit successful! Your new balance is: MK{accounts[currentAccount]['balance']:.2f}")
            except ValueError:
                print("Invalid input. Please enter a valid amount.") 
        
        elif choice == 4: #logout
            print(f"Goodbye, {accounts[currentAccount]['name']}!")
            currentAccount = None
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")
            
    except ValueError:
        print("Invalid input. Please enter a valid option (1-4).")          