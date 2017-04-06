# 136
# single number
# Given an array of integers, every element appears twice except for one. Find that single one.

'''	
[0,0,1,1,2,2,...9,9]
8 ^ 8 -> 0

8 ^ 8 ^ 9 ^ 9 -> 0

7 ^ 8 ^ 8 ^ 9 ^ 9 -> 7

if 7 ^ 8 ^ 9 == 9 ^ 8 ^ 7 -> we can xor all numbers to get the answer

xor: exclusive or
xor is commutative // 
'''

def solve(nums):
	return reduce(lambda x, y: x ^ y, nums, 0)

test = [1]
print solve(test)


