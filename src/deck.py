import random

class Deck:
    def __init__(self):
        suits = ["heart", "spade", "diamond", "club"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.cards = []

        # set up deck of cards
        for suit in suits:
            for value in values:
                self.cards.append((suit, value))

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self.cards

    def draw_card(self):
        return self.cards.pop()