# small exercise in learning how list comprehensions work

# cube numbers
def cube(n):
	return n ** 3 
	
# cube the numbers from 1- 10
print "cubes from standard list"
for i in xrange(1, 11):
	print(cube(i))

# cubes from list comprehensions
print "cubes from list comprehensions"
cube_list_comprehensions =[cube(x) for x in xrange(1, 11)]

print cube_list_comprehensions
