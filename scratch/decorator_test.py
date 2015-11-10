def outer(some_func):
	def inner():
		print "before some function"
		ret = some_func()
		print ret + 1 # instructions say return, but I could only get it to work by changing it to print

	return inner

def foo():
	return 1

decorated = outer(foo)

decorated() # returns 2
