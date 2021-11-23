# Word guessing game

import random

def word_guessing_game(turns):
    while True:

        username = input("Enter your name: ")

        print("Hello " + username + ", good luck!")

        words = ['rainbow', 'computer', 'science', 'programming',
                'python', 'mathematics', 'player', 'condition',
                'reverse', 'water', 'board', 'geeks']

        #Function to choose a random word from the words list
        word = random.choice(words)

        print("Guess the characters")

        guesses = ''

        while turns > 0:

            #count the number of times a user fails
            failed = 0

            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")

                    #for every fail, increment failed
                    failed += 1

            if failed == 0:
                print("YOU WONN!!")
                
                print("The word is: ",word)
                break

            guess = input("Guess a character: ")
            guesses += guess

            if guess not in word:
                turns -= 1

                print("Wrong")
                print("You have " + str(turns) + " more guesses")

                if turns == 0:
                    print("You lost :(")

        playagain = input("Do you want to play again? (yes or no): ").lower()

        if playagain != 'yes':
            break
    print("Good bye!")

word_guessing_game(5)

