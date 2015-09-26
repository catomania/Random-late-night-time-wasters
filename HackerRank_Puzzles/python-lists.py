# https://www.hackerrank.com/challenges/python-lists

list = []

# get the first input # which tells you many raw_inputs are following up
loop = int(raw_input())

for x in range(0, loop):
	command = raw_input()

	# modify the list according to the commands
	step = command.split(" ")


	# quite possibly the ugliest if tests I've ever produced...
	# scenarios: insert, print, remove, append, sort, pop, reverse...

	if step[0] == "insert":
		list.insert(int(step[1]), int(step[2]))

	elif step[0] == "print":
		print list

	elif step[0] == "remove":
		list.remove(int(step[1]))

	elif step[0] == "append":
		list.append(int(step[1]))

	elif step[0] == "sort":
		list.sort()

	elif step[0] == "pop":
		list.pop()

	elif step[0] == "reverse":
		list.reverse()




