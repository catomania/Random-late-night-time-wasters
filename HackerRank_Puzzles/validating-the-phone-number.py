# https://www.hackerrank.com/challenges/validating-the-phone-number

import re # I don't actually need to use regex to solve this puzzle...still not a huge fan of regex since it's hard to read

number_count = int(raw_input())

for _ in xrange(0, number_count):
	validate_me = raw_input()

	if len(validate_me) == 10: # length needs to be 10 exactly
		# if all digits
		if validate_me.isdigit() == True:
			# check if the digit starts with 7, 8, or 9

			validate_me_list = list(validate_me)
			if str(validate_me_list[0]) in ('7', '8', '9'):
				print "YES"
			else:
				print "NO"
		else:
			print "NO" 

	else:
		print "NO"
