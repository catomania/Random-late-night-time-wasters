# https://www.hackerrank.com/challenges/most-commons

# first time solving a Moderate puzzle on my own w/ a less than 80% success rate (though it took some trial and error)


from collections import Counter

string_list = []

string_input = str(raw_input())

for x in string_input:
	string_list.append(x)


my_counter = Counter(string_list) 


top_three_values = []
for i in my_counter.most_common(3): # get the top 3 letter occuranges and put them in a list for further processing

	top_three_values.append(i)

# sort by amount, and then alphabetically (element 2, and then element 1)
top_three_values_v2 = sorted(top_three_values, key = lambda x : (-x[1], x[0])) # -x[1] means descending order of 2nd element in list

for i in top_three_values_v2:

	# if the dictionary values are the same...then alphabetize?? 
	print " ".join(str(e) for e in i)

	# print out the rows without brackets or parens
