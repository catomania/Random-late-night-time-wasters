# https://www.hackerrank.com/challenges/zipped

# the zip function returns a list of iterables, where the i-th tuple contains the ith element from each of the argument sequences of iterables

# get average scores of each student

# N students X subjects

N_students, X_subjects = map(int, raw_input().split(" "))

general_mark_sheet = []

summed_list = " "
for i in range(0, X_subjects):

	# get all your test score inputs
	general_mark_sheet.append(list(map(float, raw_input().split(" "))))


# zip up your test scores and calculate the average
stuff = zip(*general_mark_sheet)

for x in stuff:

	print round(sum(x)/X_subjects, 1)
