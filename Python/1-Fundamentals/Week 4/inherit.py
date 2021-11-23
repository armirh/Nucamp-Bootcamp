class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self,password):
        self.password = password
        print("Your password has been changed to:", self.password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)


bankuser1 = BankUser("Armir", "armir@123.com","password123")
print(bankuser1.name,bankuser1.email)

bankuser1.change_password("newpassword")
bankuser1.check_balance()
print(bankuser1.password)

'''
    Challenge questions: OOP
    1. What is the purpose of the __init__ method in a class? When does it execute?
        The main purpose of the __init__ method is as a contructor. And it executes when an object
        is called from the class and to initialize the attributes of a class.
    2. What is the purpose of self parameter in a method?
        Self parameter represents the instance of a class. By using it we can access attributes and methods
        of the class in python.
    3. What is an instnace?
        Instance is an object that belongs to the class.
    4. How do you define a subclass from a superclass?
        Subclass is a class that derrives from antoher class. On the other hand, superclass is the existing class
        from which the new classes are derrived.
    5. What is the use of the super() function?
        The super method lets you access methods in the parent class.
'''