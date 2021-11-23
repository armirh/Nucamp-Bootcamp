import random


def dice_game():

    high_score = 0
    
    print("Current high score is: ", high_score)

    print("1) Roll Dice")
    print("2) Leave Game")

    choice = input("Enter your choice: ")

    if choice == "1":
        dice_roll1 = random.randint(1,6)
        print("you rolled a: ", dice_roll1)
        dice_roll2 = random.randint(1,6)
        print("You rolled a: ", dice_roll2)

        total = dice_roll1 + dice_roll2

        print("You rolled a total of: ", total)

        if total > high_score:
            print("New high score!\n")
            high_score = total

    elif choice == "2":
        print("Thank you for playing")
    else:
        print("Enter a valid choice!")
        dice_game()


dice_game()
