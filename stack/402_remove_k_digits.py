# Given a non-negative integer num represented as a string, 
# remove k digits from the number so that the new number is the smallest possible.



'''
idea

use a stack to keep track of the current digits

for every new one, 
	if is smaller than the stack top, then push it to the stack
	else
		if there are enough digits remaining, pop the top digit out ()
		else: add the rest digits to form the result

'''
