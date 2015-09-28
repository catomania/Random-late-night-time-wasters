# https://www.hackerrank.com/challenges/nested-list

# learn how to make nested lists!

i = int(raw_input())

# make nested lists 

wrapper_list = []

# create a nested list that inputs test questions
for x in range(0, i):

	child_list = []
	input_1 = raw_input()
	child_list.append(input_1)
	input_2 = raw_input()
	input_2_float = float(input_2)
	child_list.append(input_2_float)
	wrapper_list.append(child_list)	


# return names of x people that got the 2nd lowest marks in physics
s
# sort the list by the 2nd element?

wrapper_list.sort(key= lambda e:e[1]) # is sorting the best solution?

# grab lowest score and delete it from your list

lowest_score = wrapper_list[0][1]
lowest_set = wrapper_list[0]

while wrapper_list[0][1] == lowest_score: # multiple lowest scores
	wrapper_list.pop(0) # remove the true lowest scores from wrapper_list


# grab the 2nd lowest marks in physics
	name_1 = wrapper_list[0]


# if scores are identical, print names in alphabetical order
match_scores = []
for x in wrapper_list:
	if x[1] == wrapper_list[0][1]:
		match_scores.append(x[0])


# figure out what to print (either alist of names if there are matching scores, or just 1 name)
if len(match_scores) > 1:
	match_scores.sort()
	for x in match_scores:
		print x
else:
	# just print the 'new' lowest score
	print name_1[0]

