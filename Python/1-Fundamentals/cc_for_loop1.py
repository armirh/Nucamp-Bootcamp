for i in range(20, -21, -5):
    print(i)



for x in range(0,6,1):
    if x == 0 or x == 6:
        print("*")
    elif x == 1 or x == 5:
        print("**")
    elif x == 2 or x == 3:
        print("***")
    else:
        print("****")


for amount_loaded in range(0, 101, 5):
    if amount_loaded == 25:
        print("1/4 of the way there")
    elif amount_loaded == 50:
        print("Half way there")
    elif amount_loaded == 75:
        print("3/4 of the way there")
    elif amount_loaded == 100:
        print("Loading complete!")
    print(amount_loaded)


stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)

