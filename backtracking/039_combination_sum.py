'''
Given a set of candidate numbers (C) (without duplicates) 
and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
'''


# [2,3,6,7], 7

# starts with 2
# starts with 3...

# more like dfs

result = []
nums = [2,3,6,7]
def dfs(remain, i, prefix):
	if remain == 0:
		return result.append(prefix)
	for j in xrange(i, len(nums)):
		t = 1
		while nums[j] * t <= remain:
			dfs(remain-nums[j]*t, j+1, prefix + [nums[j]] * t)
			t += 1

dfs(7, 0, [])
print result


# leetcode 40
# follow up: C can have duplicate, Each number in C may only be used once in the combination.
'''
[2,2,2,3,4,4,5]
'''

'''
can still use dfs

sort the numbers

starts with 2, so we skip the following 2s
starts with 3

dfs(remain, start, prefix):
	if remain == 0: return result.append(prefix)
	for i in (start:end):
		if nums[i] == nums[i-1]: continue
		head = num[i]
		dfs(remain - head, i + 1, prefix + [num[i]])

'''




	