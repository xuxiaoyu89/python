'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
'''

'''
idea, using a stack to store prev heights in decreasing order
for a new height
if it is lower then or equal to the stack top, then push
if it is height,
	keep pop out heights until it is higher then the current one
'''

def solve(height):
	st, result, i = [], 0, 0
	while i < len(height):
		c = height[i]
		if not st or height[st[-1]] >= c:
			st.append(i)
			i += 1 
		else:
			bi = st.pop()
			if st:
				result += (min(height[st[-1]], c) - height[bi]) * (i - bi)
	return result

print solve([0,1,0,2,1,0,1,3,2,1,2,1])
