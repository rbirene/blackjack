import sys

from src.deck import Deck
from src.player import Player

def play():

    intro()

    # initialise players
    dealer = Player()
    player = Player()

    # initialise and shuffle deck of cards
    deck = Deck()
    deck.shuffle_cards()

    # deal opening hands
    dealer.add_dealer_card(deck.draw_card())
    dealer.add_dealer_card(deck.draw_card())
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())

    # while game is running, increment turn, display player info and give choice to 'hit' or 'stand' until game is over
    begin_game(dealer, player, deck)

def intro():
    print("\n=== ♠️♦️ BLACKJACK ♥️♣️ ===")
    print("The goal of the game is to get a hand of cards that is worth as close to 21 points as possible.")
    print("You can choose to ‘hit’ (draw a card) or ‘stand’ (stop drawing cards).")

def display_player_info(dealer, player, game_over):
    print("\nDealer's hand: ")
    if game_over is False:
        print("[", end="")
        print(dealer.get_card(0), end=" ")
        print(", (?, ?)]")
    if game_over is True:
        print(dealer.get_hand())
        print("Dealer total:", end=" ")
        print(dealer.get_hand_total())
    print("\nYour hand: ")
    print(player.get_hand())
    print("Your total:", end=" ")
    print(player.get_hand_total())

def begin_game(dealer, player, deck):
    game_over = False
    turn = 0
    while game_over != True:
        turn += 1
        print("\n-- TURN " + str(turn) + " --")
        if turn == 1:
            print("\nYou have been dealt your opening hand.")
        display_player_info(dealer, player, game_over)
        try:
            player_choice = input(
                "\nEnter either HIT (draw a card) or STAND (stop drawing cards) to choose what to do next: ")
        except:
            print("Invalid choice.")
            sys.exit()
        if player_choice == "HIT" or player_choice == "hit":
            player.add_card(deck.draw_card())
            if player.get_hand_total() >= 21:
                game_over = True
        elif player_choice == "STAND" or player_choice == "stand":
            game_over = True
        else:
            print("Invalid choice. You entered '" + player_choice + "'.")
            sys.exit()
    # check for winner and display end game info
    check_win(dealer, player, game_over)

def check_win(dealer, player, game_over):
    display_player_info(dealer, player, game_over)
    if player.get_hand_total() == 21 and dealer.get_hand_total() == 21:
        print("\nSTANDOFF: You have tied with the dealer 🤝")
    elif player.get_hand_total() <= 21 and player.get_hand_total() > dealer.get_hand_total():
        print("\nWIN: You have won! 🏆")
    else:
        print("\nBUST: You have lost 😢")

if __name__ == '__main__':
    play()
