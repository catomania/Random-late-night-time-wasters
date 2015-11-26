# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

# basically I didn't end up using a filter at all, I ended up using regex! Comments on this problem show others doing the same

import re
from operator import itemgetter


valid_email_count = int(raw_input())

email_list = []

for _ in range(0, valid_email_count):

	test_email = raw_input() # get the test input
	at_counter = 0 # count the number of @'s to disqualify inputs with more than 1 @ symbol

	# input disqualification tests (if they're not in a proper email format, then skip!)

	if test_email[0] == "@":
		continue

	if "." not in test_email:
		continue
			
	if "@" not in test_email:
		continue
				
	for x in test_email:
		if x == "@":
			at_counter += 1

	if at_counter > 1:
		continue # go back to main loop and skip


	# if the input passes initial disqualifying tests, then split up the email for further analysis
		
	username_email = test_email.split("@")[0]
	rest_of_email = test_email.split("@")[1]
	website_name = rest_of_email.split(".")[0]
	domain_name = rest_of_email.split(".")[1]

	# Username can only contain letters, digits, dash and underscore (had to google the re formula).
	if re.match("^[A-Za-z0-9_-]*$", username_email):
		# Website name can have letters and digits
		if re.match("^[A-Za-z0-9]*$", website_name):
			# Maximum length of the extension is 3 
			if len(str(domain_name)) < 4:
				email_list.append([str(username_email), str(website_name), str(domain_name)])

		

# sort email usernames in lexigraphical order and print email list
email_list.sort(key=itemgetter(0))

# join list back together and print out the new list
sorted_email_list = []

# print the list even if it's empty
if len(email_list) == 0:
	print email_list
else:
	for x in email_list:
		full_email = x[0] + "@" + x[1] + "." + x[2]
		sorted_email_list.append(full_email)
	print sorted_email_list	






