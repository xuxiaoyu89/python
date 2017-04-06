# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.


# thinking process
# 1. cannot go through the numbers
# 2. use m and n
# 3. the highest comman bits will survive
# 4. remove lower bits
# 5. remove from right to left

def solve(m, n):
	c = 0
	while n != m:
		n = n >> 1
		m = m >> 1
		c += 1
	return m << c

