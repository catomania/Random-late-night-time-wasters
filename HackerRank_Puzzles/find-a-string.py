# https://www.hackerrank.com/challenges/find-a-string

string = raw_input()
sub_string = raw_input()
count = 0

# strings are case sensitive

for x in range(0, len(string)):
	# does this part of the string = our substring input?

	potential_match = string[x:x+len(sub_string)] # print 0:3, 1:3... how to move 3 down the list?

	# examine substring-sized parts of the string
	if potential_match == str(sub_string):
		count += 1

print count
