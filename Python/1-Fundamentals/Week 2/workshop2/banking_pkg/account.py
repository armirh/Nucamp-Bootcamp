import sys

def show_balance(balance):
    balance = ''
    print(" Has logged in!")
    print(" The current balance is " + str(balance))

def deposit(balance):
    print("Your current balance is: " + str(balance))
    
    while True:
        deposit_amount = float(input("Enter deposit amount: "))

        balance = float()
        balance = balance + deposit_amount
        print("The new balance is: " + str(balance))
        return balance

def withdraw(balance):
    print("Current balance is: " + str(balance))

    while True:
        withdraw_amount = float(input("Enter the withdrawl amount: "))

        balance = float()
        balance = balance - withdraw_amount
        print("New balance is: " + str(balance))
        return balance

def logout():
    print("Goodbye!! ")
    sys.exit()

