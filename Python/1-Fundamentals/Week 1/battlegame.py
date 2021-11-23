
# 1.In this assignment, you will apply what you have learned this week to program a fantasy battle game.
# 2.The player will be able to choose between three characters: a Wizard, an Elf, and a Human.
# 3.The chosen character will fight a Dragon, and the program will calculate and display the results.

    #bonus task 1
    #Currently, the player only has the ability to choose their character by number: 1, 2, or 3. Also give the player the ability to choose a character by typing their name, e.g. "Wizard".

    #bonus task 2
    #Expanding on Bonus Task 2, let the user also be able to type the name in any case, such as "wizard", "WIZARD", or "WIZard", and still have it recognized as an acceptable option.

    #bonus task 3
    #Write code that will add a 4) option, such as "Orc". Initialize this character and its hitpoints and damage. 

    #bonus task 4
    #Write code that will add an option to exit from the game entirely. Then, you must figure out a way to actually cause the game to exit when this option is chosen. 

    #bonus task 5
    #Write code so that when the game is over, the player is asked if they want to play again. (Hint: You can use a loop within a loop.)

def BattleGame():
    #characters
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"
    end_game = "End Game"

    #health points
    wizard_hp = 70
    elf_hp = 100
    human_hp = 200
    orc_hp = 90
    dragon_hp = 300

    #damage points
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 105
    dragon_damage = 50
    
    characters = [wizard, elf, human, orc, end_game]

    for i, value in enumerate(characters, 1):
        print("{}.) {}".format(i, value))

    character = input("Choose your character character: ").lower()

    while True:
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == "4" or character == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif character == "5" or character == "end game":
            quit()
        print("Unknown Character")

    print("You have chosen the character:", character)
    print("Health:", my_hp)
    print("Damage:", my_damage)

    # task 4, battle with dragon
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The " , character , " has damaged the Dragon!\n")
        if dragon_hp > 0:
            print("The dragon has ", str(dragon_hp) ," left.")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle." ,character , " wins!\n")
            break
        my_hp = my_hp-dragon_damage
        print("The Dragon damaged the" ,character,"! You have ", str(my_hp) ," left!\n")
        if my_hp <= 0:
            print("The " , character , " has lost the battle!")
            break

def play_again():
    response = input("Would you like to play again? (yes/no) :").lower()
    if response == "yes":
        BattleGame()
    else:
        print("You have exited the game!")

BattleGame()
play_again()

