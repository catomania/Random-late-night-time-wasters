# https://www.hackerrank.com/challenges/the-minion-game

# Stuart: consonants

# Kevin: vowels

# please note: this program can't take really long string inputs...(and doens't pass all the hackerrank tests)
# first time working by myself on a moderate puzzle


word = str(raw_input())

consonant_list = []

vowel_list = []

for x in xrange(0, len(word)):

	if word[x] in ["A", "E", "I", "O", "U"]: # string will contain only capital letters
		# grab all vowel possible combinations 
		for i in xrange(x, len(word)+1):
			if len(word[x:i]) > 0:
				vowel_list.append(word[x:i])

	else:
		# grab all vowel possible combinations 
		for i in xrange(x, len(word)+1):
			if len(word[x:i]) > 0:
				consonant_list.append(word[x:i])


if len(vowel_list) > len(consonant_list):
	print "Kevin " + str(len(vowel_list))
elif len(consonant_list) > len(vowel_list):
	print "Stuart " + str(len(consonant_list))
else:
	print "Draw"
