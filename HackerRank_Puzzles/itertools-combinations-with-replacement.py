# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement

from itertools import combinations_with_replacement

string, size = raw_input().split(" ")

string = "".join(sorted(string)) # SORT for lexicographic order

combinations_list = list(combinations_with_replacement(list(string), int(size)))

# print combinations one by new in a new line


for x in combinations_list:
	print "".join(str(e) for e in x) # join each 2 letters and use str to remove quotes
