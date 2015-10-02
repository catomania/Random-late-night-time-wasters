# https://www.hackerrank.com/challenges/text-wrap

import textwrap
string = raw_input()
width = int(raw_input())

print textwrap.fill(string, width)
