import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame (unittest.TestCase ):

    def setUp(self):
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("hearts", 3)
        self.card_list = [self.card_1, self.card_2]
        self.card_game = CardGame
    
    def test_check_for_ace(self):
        expected = True
        actual = self.card_game.check_for_ace(self.card_1)
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = self.card_1
        actual = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        expected = 'You have a total of 4'
        actual = self.card_game.cards_total(self.card_list)
        self.assertEqual(expected, actual)