# https://www.hackerrank.com/challenges/py-introduction-to-sets

# set is an unordered collection w/o duplicate entries, the elements appear in arbitrary order
# sets are used for membership testing and eliminating duplicate entries

first_input = raw_input() #not sure why I need this, but okay?
second = set(raw_input().split(" ")) # get list values, which I then transform into a set

summed_set = sum(float(_) for _ in second) # sum up the set values, I use float on purpose instead of int here to return decimal values


print summed_set/len(second)
