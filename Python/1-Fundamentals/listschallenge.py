import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    card_select = input("Enter a card choice or Q to quit: ")

    if card_select == "Q":
        break
    else:
        card = random.choice(diamonds)
        hand.append(card)
        diamonds.remove(card)

        print("Your hand: ", hand)
        print("Remaining cards: ", diamonds)

        if not diamonds:
            print("There are no more cards!!")
        else:
            continue

