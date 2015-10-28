# https://www.hackerrank.com/challenges/exceptions

# hackerrank isn't marking "2 $" as correct becuase it marks my output as saying '$\r' (even though my output locally on sublime text says '$')

# different types of built-in exceptions: https://docs.python.org/2/library/exceptions.html#module-exceptions

number_of_inputs = int(raw_input())

for x in range(0, number_of_inputs):
	a, b = raw_input().split(" ")

	# print out either the error or the calculation

	try:
		print int(a)/int(b)

	except (ZeroDivisionError, ValueError) as e:
		print "Error Code:", e
