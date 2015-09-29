# https://www.hackerrank.com/challenges/python-mutations

string = raw_input()  # get input from test
inputs = raw_input() # get mutation inputs from test
inputs = inputs.split()

list_string = list(string) #  turn your string raw input into a list (so it's mutable)
list_string[int(inputs[0])] = str(inputs[1]) # put in the mutation edits specified

string = ''.join(list_string) # join the list together back into a string
print string
