# https://www.hackerrank.com/challenges/exceptions

# hackerrank isn't marking "2 $" as correct becuase their test is looking for a '$\r' (even though their sample output says '$')

# different types of built-in exceptions: https://docs.python.org/2/library/exceptions.html#module-exceptions

number_of_inputs = int(raw_input())

for x in range(0, number_of_inputs):
	a, b = raw_input().split(" ")

	# print out either the error or the calculation

	try:
		print int(a)/int(b)

	except (ZeroDivisionError, ValueError) as e:
		print "Error Code:", e
