# Given an array of numbers nums, in which exactly two elements appear only once 
# and all the other elements appear exactly twice. Find the two elements that appear only once.
# o(n) time and o(1) space

'''
thinking process:
we can use xor to get rid of all the numbers in pairs -> remains a ^ b

we need a way to get a and b

look into a ^ b, because a != b, there must a bit that is different.

then we can devide the array into two groups and get a and b seperately

'''


def solve(nums):
	ab = reduce(lambda x, y : x^y, nums, 0)
	bit = 1
	while bit * 2 < ab:
		bit = bit * 2
	a = reduce(lambda x, y : x^y, filter(lambda x : x & bit > 0, nums))
	b = reduce(lambda x, y : x^y, filter(lambda x : x & bit == 0, nums))
	return [a, b]

test = [0,0,1,1,2,2,4,4,5,5,3,6]
print solve(test)