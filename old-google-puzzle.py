#! python3
# googleLabs.py - attempt to try and solve an old Google recruiting question...by using BRUTE force!
# from here: https://rachelbythebay.com/w/2012/04/15/labs/
import random

vending_machine = [917, 134, 1569, 1649, 1431, 1622, 233, 2094, 1072, 915, 1922, 2437, 2714, 2491, 
1886, 2812, 426, 1673, 94, 2139, 2569, 496, 2249, 1553, 1580]


buttons = [16, 23, 61, 7, 7, 7, 13, 13, 13, 19, 19, 21, 27, 56, 56, 73, 77, 97, 11, 37, 41]

#calculate the Google vending machine formula: 


while len(vending_machine) != 1:
	#randomly sample button list
	five_buttons = random.sample(set(buttons), 5)
	#five differnet but not distinct buttons: 
	#A*B+C-D+E	
	calculation = five_buttons[0] * five_buttons[1] + five_buttons[2] - five_buttons[3] + five_buttons[4]


	#compare calculation to all items in vending machine
	for x in range(-1, int(len(vending_machine)) - 1):
		if vending_machine[x] == calculation:
			vending_machine.remove(calculation)
			print(str(vending_machine))










