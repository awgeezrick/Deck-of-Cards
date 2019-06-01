import random

class Card:
	'''
	each instance of the Card class has valid suit and value (52 instances)
	'''

	allowed_suits = ["Hearts", "Diamonds","Spades","Clubs"]
	allowed_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

	def __init__(self, suit, value):
		self.suit = suit
		if self.suit not in self.allowed_suits:
			raise ValueError (f"Please choose an existing suit")
		
		self.value = value
		if self.value not in self.allowed_values:
			raise ValueError (f"Please choose an existing value")
		

	def __repr__(self):
		'''
		__repr__ method displays the value and the suit of a card
		'''
		return f"{self.value} of {self.suit}"

class Deck:
	'''
	each instance of the Deck class has a card attribute with all 52 possible instances of Card
	'''
	def __init__(self):
		self.cards = [Card(suit,value) for suit in Card.allowed_suits for value in Card.allowed_values]

	def count(self):
		'''
		an instance method which returns the number of cards left in the deck
		'''
		return len(self.cards)

	def __repr__(self):
		'''
		an instance method which returns the information on how many cards are in the deck 
		'''
		return f"Deck of {self.count()} cards"

	def __iter__(self):
		return iter(self.cards)

	def _deal(self, num):
		'''
		an instance method which accepts a number and removes at most that many cards from the deck
		'''
		count = self.count()
		if count ==0:
			raise ValueError ("All cards have been dealt")
		actual = min([count,num])
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def shuffle(self):
		'''
		an instance method which shuffles cards if the deck is full and returns them
		'''
		if self.count() < 52:
			raise ValueError ("Only full decks can be shuffled")
		else:
			random.shuffle(self.cards)
			return self.cards

	def deal_card(self):
		'''
		an instance method which uses the _deal  method to deal a single card from the deck 
		and returns that single card.
		'''
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		'''
		an instance method which accepts a number and uses the _deal  method to deal a list of cards from the deck
		and returns that list of cards.
		'''
		return self._deal(hand_size)
