# https://www.hackerrank.com/challenges/python-sort-sort

# this is the FIRST moderate difficulty puzzle I've solved on HR!

from operator import itemgetter

N_rows, M_items = (map(int, raw_input().split(" ")))

table = []

for i in range(0, N_rows):
	table.append(map(int, raw_input().split(" ")))

k_element = int(raw_input())

# figure out how to sort the elements based on the k_element
# http://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list

my_sorted_table = sorted(table, key=itemgetter(k_element)) 

#for x in my_sorted_table:
	
for x in my_sorted_table:
	print x[0], " ".join(map(str, x[1:])) # print out the sorted table without brackets or commas
	
