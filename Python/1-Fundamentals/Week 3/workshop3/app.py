from donations_pkg.homepage import show_homepage
from donations_pkg.user import login,register,donate,show_donations

#Task 2: Show homepage and initialize app data

database = {"admin": "password"}
donations = []
authorized_users = ""

while True:
    show_homepage()

    if authorized_users == "":
        print("You must be logged in to donate")
    else:
        print("Logged in as: ", authorized_users)

    # Task 3: Handle user input
    choice = input("Enter an option from the list above: ")

    if choice == "1":
        username = input("Enter your username: ").lower()
        password = input("Enter your password: ").lower()
        authorized_users = login(database, username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if len(username) > 10:
            print("The username is too long")
        if len(password) < 5:
            print("The password must contain at least 5 chars")
        authorized_users = register(database, username)
        if authorized_users != "":
            database[username] = password
    elif choice == "3":
        if authorized_users == "":
            print("You are not logged in!")
        else:  
            donation = donate(authorized_users)
        donations.append(donation)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("Goodbye, have a good day!")
        break
    else:
        print("Enter a valid option!!!")
    continue


