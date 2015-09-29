# https://www.hackerrank.com/challenges/python-string-split-and-join

line = raw_input() # get raw input from test
line = line.split(" ") # split w/ space
line = "-".join(line) # join together by -
print line
