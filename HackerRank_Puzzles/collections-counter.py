# https://www.hackerrank.com/challenges/collections-counter

# where can I use Counter?

from collections import Counter

number_of_shoes = int(raw_input())

shoe_sizes = list(map(int, raw_input().split(" ")))

customers = int(raw_input())

money_earned = []

for x in range(0, customers):

	size, price = map(int, raw_input().split(" "))

	# check to see if the size is available in our inventory

	if size in shoe_sizes:

		shoe_sizes.remove(size) # if yes, then remove it from our inventory records

	# and add it to our profit
		money_earned.append(price)
	else:
		pass

# print out money earned

print sum(money_earned)

#print Counter(money_earned)
# I don't really see where I need to use the Counter?
