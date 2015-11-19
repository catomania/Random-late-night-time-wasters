# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators

number_count = int(raw_input())

phone_numbers_list = []

for x in range(0, number_count):

	phone_number = str(raw_input())

	# check input formatting and revise as needed
	if phone_number[0] == "0":
		phone_number = phone_number[1:len(phone_number)]
	elif len(phone_number) > 10 and phone_number[0:2] == "91":
		phone_number = phone_number[2:len(phone_number)]
	elif len(phone_number) > 10 and phone_number[0:3] == "+91":
		phone_number = phone_number[3:len(phone_number)]


	phone_numbers_list.append(int(phone_number))


def my_decorator(some_func):
	def real_decorator():
		foo = some_func()
		# because we want to use decorators to reformat a phone number
		for x in foo: # now foo is what is returned from sorted_list()
			print "+91 " + str(x)[0:5] + " " + str(x)[5:11]
	return real_decorator

def sorted_list(): # puzzle wants the phone number sorted in ascending order
	phone_numbers_list_sorted = sorted(phone_numbers_list)
	return phone_numbers_list_sorted


decorated = my_decorator(sorted_list)

decorated() # you don't need to print this, if you do, you'll get an extra "none" returned to you

