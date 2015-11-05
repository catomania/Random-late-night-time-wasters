# https://www.hackerrank.com/challenges/map-and-lambda-expression

fibonacci_count = int(raw_input())

# us the lambda function (single anonymous function)
cubed = lambda a: a * a * a

# my fibs 
fib_one = 0
fib_two = 1
my_fib_list = [fib_one, fib_two]
cubed_list = []


# make 15 fibs:
for x in range(1, 14): # already inserted the first 2 values, the test limits are including values from 0 to 15
	new_value = int(my_fib_list[x-1]) + int(my_fib_list[x])
	my_fib_list.append(new_value) # add in new fibonacci values


# cube my fib list and make sure I only display the right amount of fibonacci numbers
print (map(cubed, my_fib_list[0:fibonacci_count]))



