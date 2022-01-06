# :spades: :diamonds: Blackjack :hearts: :clubs:

This code is a simplified version of the classic card game, Blackjack.


## The Game

The goal of the game is for the player to get a hand of cards that is worth less than or is 21 points and beat the dealer's hand.

The player and dealer are initially dealt two cards. Only the dealer's first card can be viewed by the player, the second card remains hidden until the end of the game.

Once the opening hand has been dealt, the player can choose to either:
- HIT: draw a card
- STAND: stop drawing cards

If they HIT, then the new card's value is added to their hand total. If they STAND, then their score is evaluated.

- If a player's hand total goes over 21 points, then the player is BUST, and loses
- If their hand is less than or is 21, and is higher than the dealer's hand total, then player wins
- If their hand is 21 and the dealer's hand is also 21, then it is a STANDOFF and the player ties with the dealer

## Set Up

- Requires Python 3
- Run the game:
  - From the project directory, type in terminal: `python3 blackjack.py`
- Run the unit tests:
    - From the project directory, type in terminal: `python3 -m unittest discover test`
    
## Assumptions Made

In order to focus on coding a simple functioning game of Blackjack instead of the details and variations of how the game can be played, the following assumptions have been made:

- Assume only one player (and one dealer which is handled by the program)
- Assume single deck used, and deck consists of 52 cards, shuffled to keep order random
  - Card can be taken off the deck and added to a hand
- Assume two cards are initially dealt for each opening hand (for player and dealer)
  - Player’s hand is visible to player at each turn 
  - Only the first card from the dealer’s hand is visible to the player at each turn, the second card is hidden until the end of the game
- Assume player chooses between two options at each turn:
  - HIT: draw a card (and update the hand total score)
  - STAND: stop drawing cards (and evaluate the hand total score)
- Assume Ace can have a value of either 1 or 11, and this value can be chosen by player (or chosen randomly for dealer)
- Assume face cards (i.e. Jack, Queen, King) have a value of 10
- Assume all other cards are valued at their numeric count (e.g. 4 of Spades has a value of 4)
- Assume player has only three possible endings:
  - BUST: If player's hand total goes over 21 points, then player is BUST and loses 
  - WIN: If player's hand is less than or is 21, and is higher than the dealer's hand total, then player wins 
  - STANDOFF: If player's hand is 21 and the dealer's hand is also 21, then it's a STANDOFF and the player ties with the dealer

## User Scenarios

**Scenario 1**  
Given I play a game of blackjack  
When I am dealt my opening hand  
Then I have two cards

**Scenario 2**  
Given I have a valid hand of cards  
When I choose to ‘hit’  
Then I receive another card  
And my score is updated  

**Scenario 3**  
Given I have a valid hand of cards  
When I choose to ‘stand’  
Then I receive no further cards  
And my score is evaluated  

**Scenario 4**  
Given my score is updated or evaluated  
When it is 21 or less  
Then I have a valid hand  

**Scenario 5**  
Given my score is updated  
When it is 22 or more  
Then I am ‘bust’ and do not have a valid hand  

**Scenario 6**  
Given I have a king and an ace  
When my score is evaluated  
Then my score is 21  

**Scenario 7**  
Given I have a king, a queen, and an ace  
When my score is evaluated  
Then my score is 21  

**Scenario 8**  
Given that I have a nine, an ace, and another ace  
When my score is evaluated  
Then my score is 21  

## Future Improvements

There are multiple ways this project could be improved upon in the future:
- Implement feature that ensures dealer will always HIT until hand total is 17 or more
- Allow for multiple players to play the game at once
- Implement a betting feature to allow players to bet (e.g. player has predefined number of chips which can be added to or subtracted based on gameplay)
- Create a frontend to view a visual representation of the game and allow users to interact with the UI (e.g. HIT button on a React frontend sends feedback to Python backend to update player hand and total, removes need for user input in the terminal and reduces risk of invalid input by choosing from predefined options)
