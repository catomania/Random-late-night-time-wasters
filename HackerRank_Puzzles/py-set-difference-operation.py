# https://www.hackerrank.com/challenges/py-set-difference-operation


english_subs = raw_input() # I don't even use this...


# turn english roll into integers
english_roll_set = set(map(int, raw_input().split(" ")))


french_subs = raw_input() # I don't even use this...

# turn french roll into integers
french_roll_set = set(map(int, raw_input().split(" ")))


# return back roll of students who have at least one subscription
print len(english_roll_set.difference(french_roll_set))
