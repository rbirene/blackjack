import sys
import random

class Player:
    def __init__(self):
        self.hand = []
        self.total = 0

    # calculate total score of current cards in player's hand
    def calculate_hand_total(self):
        face = ["J", "Q", "K"]
        self.set_hand_total(0)
        for card in self.hand:
            if card[1] in range(1, 12):
                self.total += card[1]
            elif card[1] in face:
                self.total += 10

    # add new card to player's hand
    def add_card(self, card):
        ace_value = ""
        if card[1] == "A": # if Ace, then give option to choose card value to be either 1 or 11
            try:
                ace_value = input("\nYou have received an Ace! Please enter either 1 or 11 for the Ace value: ")
            except:
                print("Invalid value.")
                sys.exit()
            if ace_value == "1" or ace_value == "11":
                ace_card = (card[0], int(ace_value), "A")
            else:
                print("Invalid value. You entered '" + ace_value + "'.")
                sys.exit()
            self.hand.append(ace_card)
        else:
            self.hand.append(card)
        self.calculate_hand_total() # update player's hand total
        return

    # add new card to dealer's hand
    def add_dealer_card(self, card):
        if card[1] == "A":  # if Ace, then give randomly choose card value to be either 1 or 11
            ace_value = random.choice([1, 11])
            ace_card = (card[0], int(ace_value), "A")
            self.hand.append(ace_card)
        else:
            self.hand.append(card)
        self.calculate_hand_total() # update dealer's hand total
        return

    def set_hand_total(self, new_total):
        self.total = new_total

    def get_hand(self):
        return self.hand

    def get_hand_total(self):
        return self.total

    def get_card(self, card):
        return self.hand[card]