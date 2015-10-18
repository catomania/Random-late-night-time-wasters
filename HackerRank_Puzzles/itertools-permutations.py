# https://www.hackerrank.com/challenges/itertools-permutations

from itertools import permutations

string, iterable = raw_input().split(" ")

string = "".join(sorted(string)) # SORT for lexicographic order

permutation_list = list(permutations(list(string), int(iterable)))

# print permutations one by new in a new line


for x in permutation_list:
	print "".join(str(e) for e in x) # join each 2 letters and use str to remove quotes?
