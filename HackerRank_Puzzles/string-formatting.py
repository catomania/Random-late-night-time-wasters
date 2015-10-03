# https://www.hackerrank.com/challenges/python-string-formatting

n = int(raw_input())

for i in range(1, n+1):

	padding = len(bin(n))-2 # binary needs the first 2 characters removed

	
	

	# octal needs leading 0 removed


	string = str(i)
	
	octal = oct(i) # octal needs leading 0 removed
	octal_format = octal [1:len(octal)]

	hexi = hex(i) # hexi needs first 2 characters removed
	hexi_format = str(hexi [2:len(hexi)]).upper()

	binary = bin(i) # binary needs the first 2 characters removed
	binary_format = binary [2:len(binary)]

	# how do I make padding even?

	print string.rjust(padding) + octal_format.rjust(padding+1) + hexi_format.rjust(padding+1) + binary_format.rjust(padding + 1)
