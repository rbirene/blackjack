import unittest

from src.player import Player


class DeckTestCase(unittest.TestCase):

    def setUp(self):
        self.dealer = Player()  # initialise dealer
        self.player = Player() # initialise player

    def tearDown(self):
        pass

    # test card is added to player hand
    def test_add_card(self):
        card = ("diamond", 9)
        self.player.add_card(card)
        self.assertListEqual([("diamond", 9)], self.player.get_hand())

    # test card is added to dealer hand and ace value should randomly choose between 1 or 11
    def test_add_dealer_card(self):
        card = ("heart", "A")
        self.dealer.add_dealer_card(card)
        dealer_card = self.dealer.get_card(0)
        self.assertTrue(dealer_card[1] == 1 or dealer_card[1] == 11)

    # test multiple cards are added to player hand
    def test_add_multiple_cards(self):
        card1 = ("diamond", 9)
        card2 = ("spade", 4)
        self.player.add_card(card1)
        self.player.add_card(card2)
        self.assertCountEqual([("diamond", 9), ("spade", 4)], self.player.get_hand())

    # test hand total is calculated correctly
    def test_calculate_hand_total(self):
        card1 = ("spade", "A")
        card2 = ("club", "J")
        self.player.add_card(card1)
        self.player.add_card(card2)
        self.assertEqual(21, self.player.get_hand_total())

if __name__ == '__main__':
    unittest.main()
