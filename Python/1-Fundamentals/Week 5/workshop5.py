import random

def guess_random_number(tries,start,stop):
    
    target_number = random.randrange(start,stop)

    while tries != 0:
        print("Number of tries remaining: ",tries)

        guess = int(input("Guess a number between 0 and 10: "))
        
        if guess == target_number:
            print("You have guessed the correct number")
            break
        elif guess > target_number:
            print("Guess lower!")
            tries -= 1
        elif guess < target_number:
            print("Guess higher!")
            tries -= 1
        
        if tries == 0:
            print("You have failed to guess the number: ", target_number)

#guess_random_number(5,0,10)


def guess_random_num_linear(tries,start,stop):

    guess = random.randrange(start,stop)

    print("The number for the program to guess is: ",guess)
    print("Number of tries left: ", tries)

    for i in range(guess):
        if i != guess:
            print("The program is guessing...", i)
            tries -= 1
            print("Number of tries left: ",tries)
        if i == guess:
            print("The program has guessed the correct number!")
            break
        if tries == 0:
            print("The program has failed to guess the correct number!")
            break

#guess_random_num_linear(5,0,11)


def guess_random_num_binary(tries,start,stop):

    target = random.randrange(start,stop)
    print(f"Random number to find {target}")

    while tries != 0:
        if start < stop:
            pivot_value = (start + stop) // 2

        if pivot_value == target:
            print(f"Found it {target}")
            return
        elif pivot_value < target:
            start = pivot_value + 1
            print("Guessing lower!")
        elif pivot_value > target:
            stop = pivot_value - 1
            print("Guessing higher!")

        tries -=1

        if tries == 0:
            print("Your program has failed to find the number")
            break

#guess_random_num_binary(5,0,100)

