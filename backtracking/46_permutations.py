# Given a collection of distinct numbers, return all possible permutations.

# use recursion


# 1,2,3

'''
pick first one, pick second one in the rest of the numbers, so on and so on
'''

result = []
def solve(prefix, nums):
	if not nums: result.append(prefix)
	for i in xrange(len(nums)):
		solve(prefix+[nums[i]], nums[0:i] + nums[i+1:])



# follow up: what if they are not distinct? leetcode 47
# 2,2,3

'''
similar idea, pick the first one, if it is the same first one as last time, ingore
first 2, second 2, ...
first 2 -> same as last time, then ingore
first 3, second 2, ...
'''

result = []
def solve(prefix, nums):
	if not nums: result.append(prefix)
	for i in xrange(len(nums)):
		if i == 0 or nums[i] != nums[i-1]:
			solve(prefix+[nums[i]], nums[0:i] + nums[i+1:])

l = [1,2,2,3]
solve([], l)
print result



# use loops
# for each num, insert it in each position.
# if not unique, insert from end, if insert before the same element, then stop inserting for this temp result
'''
1,2,2 -> 
[1]
[1,2],   |  [2,1]
[1,2,2], |  [2,1,2], [2,2,1]


















