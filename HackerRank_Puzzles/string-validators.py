# https://www.hackerrank.com/challenges/string-validators

string_s = str(raw_input())

results_1 = [] #isalnum test
results_2 = [] #isalpha test
results_3 = [] #isdigit test
results_4 = [] #islower test
results_5 = [] #isupper test

# any alphanumeric test
for x in string_s:
	results_1.append(str(x.isalnum()))
	results_2.append(str(x.isalpha()))
	results_3.append(str(x.isdigit()))
	results_4.append(str(x.islower()))
	results_5.append(str(x.isupper()))

if 'True' in results_1:
	print 'True'
else:
	print 'False'

if 'True' in results_2:
	print 'True'
else:
	print 'False'

if 'True' in results_3:
	print 'True'
else:
	print 'False'

if 'True' in results_4:
	print 'True'
else:
	print 'False'

if 'True' in results_5:
	print 'True'
else:
	print 'False'
