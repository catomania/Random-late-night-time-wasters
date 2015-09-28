# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
# does not pass all tests :(

# 1st raw input
integer = int(raw_input())

#2nd raw input
second_input = raw_input() # 50 100 50

# 1 -1 -2 -1


list = []


splitted = second_input.split(" ")

for x in range(0, integer):
	list.append(int(splitted[x])) # need to convert to integer, otherwise max function doesn't work


# get current max value of your list
max_value = max(list)

# remove ALL max values from your list
while max(list) == max_value:
	list.remove(max_value)

# print out the new max value (which is the 2nd largest value from your original list)
print max(list)
