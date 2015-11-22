# https://www.hackerrank.com/challenges/decorators-2-name-directory

from operator import itemgetter

number_of_inputs = int(raw_input())

parent_list = []

for x in range(0, number_of_inputs):

	first_name, last_name, age, gender = map(str, raw_input().split(" "))

	entry_list = []

	entry_list.extend([first_name, last_name, int(age), gender])

	parent_list.append(entry_list)


# sort by age
parent_list.sort(key=itemgetter(2))

x_parent_list_counter = 0


def male_or_female():
	x_parent_list_counter = 0
	for x in parent_list:
		for i in range(0, len(x)):
			if x[i] == "M":
				parent_list[x_parent_list_counter][i] = "Mr."
				
			if x[i] == "F":
				parent_list[x_parent_list_counter][i] = "Ms."
		x_parent_list_counter += 1 
	return parent_list

def decorator_format(a_function):
	def inner_decorator():
		my_function = a_function() 
		for x in my_function:
			print x[3] + " " + x[0] + " " + x[1]
	return inner_decorator	

decorated = decorator_format(male_or_female)

decorated()
