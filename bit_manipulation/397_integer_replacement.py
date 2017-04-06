'''
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?
'''

# so question is, do we do plus or minus for n?
# ___01 -> -1, we can get two trailing zeros
# ___11 -> +1, we can also get two trailing zeros,
# except 3

def solve(n):
	result = 0
	while n != 1:
		if n % 2 == 0:
			n /= 2
		elif n % 4 == 1 or n == 3:
			n -= 1
		else:
			n += 1
		result += 1
	return result

print solve(14)
