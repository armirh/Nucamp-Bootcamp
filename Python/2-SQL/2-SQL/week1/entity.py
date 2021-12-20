import datetime

# Entities are a named object composed of data fields(Attributes)
# Attributes can be of any primitive data type, e.g. integer, string, bolean

# in our case, User is the entity
# and the attributues are username, password, and birthdate

class User:
    username = "admin"
    password = "admin123"
    birthdate = datetime.datetime.now()

u1 = User()
print(u1.username, u1.password, u1.birthdate)

