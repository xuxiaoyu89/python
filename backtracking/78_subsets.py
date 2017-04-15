'''
Given a set of distinct integers, nums, return all possible subsets.
Note: The solution set must not contain duplicate subsets.
'''


# 1,2,3

'''
for every number, there are two options: choose or not choose
[]
[] [1]
[] [1] [2] [1,2]
[] [1] [2] [1,2] [3] [1,3] [2,3] [1,2,3]
'''