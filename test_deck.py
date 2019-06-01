import unittest
from deck import Card, Deck

class TestCard(unittest.TestCase):

	def setUp(self):
		self.card = Card("Hearts", "A")

	def test_init(self):
		self.assertEqual(self.card.value, "A")
		self.assertEqual(self.card.suit, "Hearts")


	def test_repr(self):
		self.assertEqual(repr(self.card), "A of Hearts")


class TestDeck(unittest.TestCase):

	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		self.assertIsInstance(self.deck.cards, list)

	def test_count(self):
		self.assertEqual(len(self.deck.cards), 52)
		self.deck.cards.pop()
		self.assertEqual(len(self.deck.cards),51)

	def test_repr(self):
		self.assertEqual(repr(self.deck), 'Deck of 52 cards')

	def test_deal_some(self):
		cards = self.deck._deal(5)
		self.assertEqual(len(cards), 5)
		self.assertEqual(self.deck.count(), 47)

	def test_deal_all(self):
		cards = self.deck._deal(60)
		self.assertEqual(len(cards),52)
		self.assertEqual(self.deck.count(),0)

	def test_deal_no_cards(self):
		self.deck._deal(52)
		with self.assertRaises(ValueError):
			self.deck._deal(1)

	def test_deal_cards(self):
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(self.deck.count(),51)

	def test_deal_hand(self):
		cards = self.deck.deal_hand(12)
		self.assertEqual(len(cards),12)
		self.assertEqual(self.deck.count(),40)

	def test_shuffle_unsufficient(self):
		self.deck._deal(10)
		self.assertEqual(self.deck.count(),42)
		with self.assertRaises(ValueError):
			self.deck.shuffle()


	def test_shuffle_sufficient(self):
		clone_cards = self.deck.cards[:]
		self.deck.shuffle()
		self.assertEqual(self.deck.count(),52)
		self.assertNotEqual(clone_cards, self.deck.cards)



if __name__ == "__main__":
	unittest.main()