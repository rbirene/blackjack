import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck() # initialise deck
        self.deck.shuffle_cards() # shuffle cards in deck

    def tearDown(self):  # this method will be run after each tests
        pass

    # test correct number of cards in the deck
    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

if __name__ == '__main__':
    unittest.main()
