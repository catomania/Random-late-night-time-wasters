# please note: I don't think the answers I have will pass the tests. 
#https://www.hackerrank.com/challenges/python-quest-1


# attempt 1:
addition = 1

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
	new_value = addition * i
	print new_value
	addition = (addition * 10) + 1
	
