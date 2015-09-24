# https://www.hackerrank.com/challenges/finding-the-percentage

list = []

# grab all the inputs

lines = raw_input() 

for x in range(0, int(lines)+1):
	scores = raw_input()
	list.append(scores)

name_match = list[-1]

# remove the 'name' from the list (last input value)
list.remove(name_match)

dict2 = []

for x in list:
	one = x.split(" ")
	name = one[0]

	score_1 = one[1]
	score_2 = one[2]
	score_3 = one[3]

	t = {name: score_1} # put these values into a dictionary
	y = {name: score_2}
	z = {name: score_3}

	dict2.append(t) # stuff it all into a list
	dict2.append(y)
	dict2.append(z)


score = []


for l in dict2:
	if (name_match in l):
		score.append(l[name_match])

# get average the scores

average_score = (float(score[0]) + float(score[1]) + float(score[2])) / 3


# print w/ decimal places
average_score = format(average_score, '.2f')

print average_score
