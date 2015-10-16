# https://www.hackerrank.com/challenges/polar-coordinates

# success rate for this puzzle is 85.75%, which makes it still harder than the python-sort-sort puzzle... 

from cmath import * 
# take complex z and convert to polar coordinate

test_inputs = raw_input()

input_count = -1
# sample input: 1+2j

for x in test_inputs: # check to see if the input needs a + or - delimiter

	input_count += 1 # get the position of which x you're on
	
	if x == "+":

		x_variable, yj_variable = test_inputs.split("+")

		break

	else: # if it's a -1-2j or a 1-2j
		if x.isdigit() == False and input_count > 0:
			
			test_inputs_list = list(test_inputs)

			test_inputs_list[input_count] = '*'


			test_inputs = (''.join(test_inputs_list))



			# swap out the 2nd minus for an asterisk
				
			x_variable, yj_variable = test_inputs.split('*') #split at the end minus

			yj_variable = '-' + yj_variable # put the minus back in, because I don't know how to split aside from using a delimiter... jesus christ...

			break


x_variable = float(x_variable) # convert to float

yj_variable_list = list(yj_variable) # start the process of removing the last "j" from YJ

yj_variable_list.pop()

#y_variable = abs(float(str(''.join(yj_variable_list)))) # convert the yj part into an abs float

y_variable = float(str(''.join(yj_variable_list)))

# return value of r, distance from z to origin

print abs(complex(x_variable, y_variable))



# return value of Phi (I do not yet understand the math behind this)

print phase(complex(x_variable, y_variable))
