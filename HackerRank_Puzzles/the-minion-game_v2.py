# https://www.hackerrank.com/challenges/the-minion-game

# Stuart: consonants

# Kevin: vowels

# this passes all the tests but I'm a tiny bit miffed that we can't use len() without the timing out on the tests...


word = str(raw_input())

word_length = int(len(word))

vowel_counter = 0

consonant_counter = 0

count_up = 0

for x in xrange(0, len(word)):


	if word[x] in ["A", "E", "I", "O", "U"]: # string will contain only capital letters
		
		# how to mathematically count up the possible vowel combinations
		vowel_counter += ((word_length)-(count_up)) # don't use len here, that takes too much processing time

	else:
		consonant_counter += ((word_length)-(count_up))

	count_up += 1 # you use this instead of len because it takes less processing time

if vowel_counter > consonant_counter:
	print "Kevin " + str(vowel_counter)
elif consonant_counter > vowel_counter:
	print "Stuart " + str(consonant_counter)
else:
	print "Draw"


