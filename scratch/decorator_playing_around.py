# from http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

class Coordinate(object):
	def __init__(self, x, y): # actually 2 parameters
		self.x = x
		self.y = y
	def __repr__(self):
		return "Coord: " + str(self.__dict__) # where is dict coming from?

def add(a, b):
	print Coordinate(a.x + b.x, a.y + b.y) # this cannot be return, needs to be print

def sub(a, b):
	print  Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 100)
two = Coordinate(200, 300)

add(one, two)
sub(one, two)
