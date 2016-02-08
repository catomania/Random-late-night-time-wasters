#Assume you have a method isSubstring which checks if one word is a
#substring of another. Given two strings, s1 and s2, write code to check if s2 is
#a rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a rotation of "erbottlewat").



def rotatedStringHasSubstring(s1, s2):
	# make sure s1 and s2 are of the same length
	if len(s1) != len(s2):
		return False
	else:
		# rotation = moving letters from front to back but not mixing up letters
		# make an s1s1 string
		double_s1 = s1 + s1

		# call isSubstring and return the results
		return isSubstring(double_s1, s2) 

def isSubstring(s1, s2):
	# is s2 a substring s1
	# http://www.tutorialspoint.com/python/string_find.htm
	# returns either True or False
	return s1.find(s2) > -1

#testing


if rotatedStringHasSubstring("waterbottle", "erbottlewat"):
	print "Passed test 1!"

if not rotatedStringHasSubstring("catnaps", "pinkys"):
	print "Passed test 2!"
