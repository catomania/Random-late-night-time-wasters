# the * operator: any extra positional arguments passed to the function end up in teh variable prefaced w/ a *

def one(*args):
	print args

one()

one(1, 2, 3)

def two(x, y, *args): # catch additional parameters in args
	print x, y, args

two(1, 2, 3, 4)

# * can extract all variable contents

def add(x, y):
	return x + y

list = [1, 2]

print add(list[0], list[1])

print add(*list) # when a * is added to the called function, all variable contents are extracted

# double asterisk: extracts all dictionary and k/v pairs

def double_asterisk(**kwargs):
	print kwargs

print double_asterisk(x=1, y=2, z=3)
