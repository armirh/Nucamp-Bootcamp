class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self,new_name):
        self.name = new_name
        if len(new_name) >= 2 and len(new_name) <=10: 
            return new_name
        else:
            print("Pick a new name between 2 and 10 characters")

    def change_pin(self,new_pin):
        self.pin = new_pin
        if len(new_pin) == 4:
            return new_pin
        else:
            print("Your pin is invalid")

    def change_password(self,new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name,pin,password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self,withdraw_amount):
        self.withdraw = withdraw_amount
        self.balance = self.balance - withdraw_amount

    def deposit(self,deposit_amount):
        self.deposit = deposit_amount
        self.balance = self.balance + deposit_amount

    def transfer_money(self,user,amount):
        print("You are transferring $",amount," to ", user.name)
        print("Authentication required")
        pin_number = int(input("Enter your pin number: "))
        if self.pin == pin_number:
            print("Transfer authorized")
            print("Transfering $" ,amount ,"to" ,user.name)
            self.balance = self.balance - amount
            user.balance = user.balance + amount
            return True
        else:
            print("Invalid PIN")
            return False

    def request_money(self,user,amount):
        print("You are requesting $", amount, " from",user.name)
        print("User Authentication required")
        pin_number = int(input("Enter PIN: "))
        password_input = input("Enter your password: ")
        print("Request authorized " if (pin_number == user.pin and password_input == self.password) else "Invalid Credentials")
        print(user.name, "sent $", amount)
        self.balance = self.balance - amount
        user.balance = user.balance + amount

""" Driver Code for Task 1 """
#user1 = User(name="Bob",pin="1234",password="password")
#print(user1.name,user1.pin,user1.password)


""" Driver Code for Task 2 """
#print(user1.change_name("Bobby"), user1.change_pin("4321"), user1.change_password("newpassword"))


""" Driver Code for Task 3
user2 = BankUser(name="Bob",pin="1234",password="password")
print(user2.name, user2.pin, user2.password,user2.balance)"""


""" Driver Code for Task 4
user3 = BankUser(name="Bob", pin="1234",password="password")
user3.show_balance()
user3.deposit(1000)
user3.show_balance()
user3.withdraw(500)
user3.show_balance()"""



"""Driver Code for Task 5
user1 = BankUser("Bob", 1234, "password")
user2 = BankUser("Alice", 1234, "alicepassword")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()
user2.transfer_money(user1, 500)
user1.show_balance()
user2.show_balance()
user1.request_money(user1, 200)
user2.show_balance()
user1.show_balance()"""






