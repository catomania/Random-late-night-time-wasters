# http://pythoncentral.io/introduction-to-python-classes/

# card1 = CARD(Card.SPADES, 2) printed should yield '2 of Spades'

class Card:
	# define suits
	SPADES = 0 # set variables for the SUITS dict
	SUITS = {
	SPADES: 'Spades'
	}

	def __init__(self, suit, value):
		self.suit = suit # member variables
		self.value = value 

	def __str__(self): # what if I name this something else?
		card_number = str(self.value)
		card_suit = str(self.SUITS[self.suit])

		return card_number + " of " + card_suit



card1 = Card(Card.SPADES, 2)

print card1

# from http://www.programiz.com/article/python-self-why (talks about how you can add in new function to a calss)

class Foo:
	def __init__(self, val):
		self.val = val


obj = Foo(42)

def printVal(self): # created outside the class, all you need to do is use (self)
	print(self.val)

Foo.printVal = printVal # add printVal function to the Foo class
obj.printVal() 



















