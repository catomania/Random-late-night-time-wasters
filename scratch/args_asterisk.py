# the * operator: any extra positional arguments passed to the function end up in teh variable prefaced w/ a *

def one(*args):
	print args

one()

one(1, 2, 3)

def two(x, y, *args): # catch additional parameters in args
	print x, y, args

two(1, 2, 3, 4)
