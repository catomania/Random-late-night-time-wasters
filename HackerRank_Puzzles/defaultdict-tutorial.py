# https://www.hackerrank.com/challenges/defaultdict-tutorial

# my 2 cents: what baffles me is that there is NO reason to use a Default Dict to solve this puzzle!

from collections import defaultdict

A = defaultdict(list) # I only use defaultdict here because the test is supposedly on defaultdicts
B = defaultdict(list)


place_counter = 1 # return the list place for A if needed

n, m = map(int,raw_input().split(" ")) # assign variables to the raw input values using map(function, iterable) 

# put a's values into A's default dict 
for _ in range(0, n):
	A['something'].append(raw_input())


# put b's values into B's default dict
for _ in range(0, m):
	B['dict_2'].append(raw_input())

# return back m lines of where b's values occur in A

for x in B['dict_2']: # for the number of lookup values (from list B)...

	generated_list = []  # create a fresh list to store your positions per element on List B
	place_counter = 1 # assign placement values as you are going through A trying to find your B values
	
	for y in A['something']: # look through all the A values
		if x == y: # if there is a match
			generated_list.append(place_counter) # then record the match's position on List A


		place_counter += 1 # each time you move an element on List A, increase your count

	if not generated_list: # if no matches for x in B, return -1 (as specified in the test)
		print "-1"
	else:
		print " ".join(str(z) for z in generated_list) # if there are matches, then print matches w/ spaces in between
