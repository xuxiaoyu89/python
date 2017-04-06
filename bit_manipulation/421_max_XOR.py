'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
Could you do this in O(n) runtime?
'''


# naive way: iterate each combination -> o(n**2) running time

# think about trie: we can build a trie with all the numbers in o(n) time, 
# and then find the best companion for each one in constant time

# conclusion: trie can speed up search and reduece memory usage.


def solve(nums):
	root = {}
	for s in map(lambda x: '{:032b}'.format(x), nums):
		curr = root
		for c in s:
			c = int(c)
			if c not in curr:
				curr[c] = {}
			curr = curr[c]
	result = 0
	for s in map(lambda x: '{:032b}'.format(x), nums):
		curr = root
		temp = 0
		for c in s:
			if 1-int(c) in curr:
				curr = curr[1-int(c)]
				temp = temp*2 + 1
			else:
				curr = curr[int(c)]
				temp *= 2
		result = max(result, temp)
	return result
