#https://www.hackerrank.com/challenges/py-set-add

upper_limit = int(raw_input())

countries = set()

for _ in range(0, upper_limit):
	#add_country = raw_input()
	countries.add(raw_input())

print len(countries)
