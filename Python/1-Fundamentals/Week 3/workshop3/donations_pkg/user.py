#Task 4: Login functionality
# In its parameter list, define three parameters: database, username, and password.

def login(database, username, password):
    if username in dict.keys(database) and database[username] == password:
        print("Welcome back: ", username)
    elif username in dict.keys(database) or password in dict.values(database):
        print("Check your credentials again!")
    else:
        print("Something went wrong")

def register(database, username):
    if username in dict.values(database):
        print("Username already registered")
    else:
        print("Username successfully registered: ", username)

def donate(username):
    donation_amount = float(input("Enter an amount to donate: "))
    donation = f'{username} donated ${donation_amount}'
    return donation

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("There are currently no donations")
    else:
        for d in donations:
            print(d)


