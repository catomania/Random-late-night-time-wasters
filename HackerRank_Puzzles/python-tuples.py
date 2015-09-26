# https://www.hackerrank.com/challenges/python-tuples

# I solved this in a...weird way since I have never used the map function before.

# hold our values
list = []


# get tuple size (you don't really need this?)
count = raw_input()	


list_value = raw_input() #2nd line if inputs from the puzzle

list = list_value.split() #split by spaces, but now it has these ugly '' marks

list = [int(a) for a in list] #convert the elements of the list into integers


# turn list into integers...

t = tuple(list)

hashed = hash(t)

print hashed

