'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Now your job is to find the total Hamming distance between all pairs of the given numbers.
'''

# distance -> only 0 and 1 in the same positions can add to distance
# keep track of number of 0s and 1s in each position, then sum (1s * 0s)

def solve(nums):
	pairs = [[0,0] for _ in xrange(32)]
	for n in nums:
		for i in xrange(32):
			pairs[i][n & 1] += 1
			n >>= 1
	return sum(map(lambda x: x[0] * x[1], pairs))


