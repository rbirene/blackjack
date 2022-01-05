## Blackjack

This code is a simplified version of the classic card game, Blackjack.


### The Game

The goal of the game is for the player to get a hand of cards that is worth less than or is 21 points and beat the dealer's hand.

The player and dealer are initially dealt two cards. Only the dealer's first card can be viewed by the player, the second card remains hidden until the end of the game.

Once the opening hand has been dealt, the player can choose to either:
- HIT (draw a card)
- STAND (stop drawing cards)

If they HIT, then the new card's value is added to their hand total. If they STAND, then their score is evaluated.

- If a player's hand total goes over 21 points, then the player is BUST, and loses
- If their hand is less than or is 21, and is higher than the dealer's hand total, then player wins
- If their hand is 21 and the dealer's hand is also 21, then it is a STANDOFF and the player ties with the dealer

### Set Up

- Install Python 3
- Run the game:
  - From the project directory, type in terminal: `python3 blackjack.py`
- Run the unit tests.
    - From the project directory, type in terminal: `python3 -m unittest discover test`
    