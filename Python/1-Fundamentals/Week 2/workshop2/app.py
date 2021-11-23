from os import name
from banking_pkg.account import show_balance,deposit,withdraw,logout

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    '''
            #Task 2
            Registration
    '''
    #declare a name and input
    name = input("Enter name to register: ")
    pin = input("Enter your PIN number: ")
    balance = 0

    print(name + " has been registered with a starting balance of " + str(balance))

    print("\n------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("\n------------------------------------------")


    '''     Task #3 
            Log in and prompt for menu option
    '''

    while True:
        validate_name = input("Enter name: ")
        validate_pin = input("Enter PIN: ")

    
        if validate_name == name and validate_pin == pin:
            print("Login successful!")
            break
        else:
            print("Invalid credentials!")

        #bonus task 2
        if len(validate_pin) >= 5:
            print("Pin must contain 4 numbers!")

        #bonus task 1
        if len(validate_name) >= 10:
            print("The maximum name length is 10 characters.")

while True:
    atm_menu(name)
    menu_option = input("Choose an option: ")
    balance = ''
    if menu_option == "1":
        show_balance(balance)
        continue
    elif menu_option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif menu_option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif menu_option == "4":
        logout()
    else:
        print("Invalid input!!!")
        print()


