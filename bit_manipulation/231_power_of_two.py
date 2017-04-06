# check if a number is power of 2

# intuitive way:
# def solve(n):
# 	t = 1
# 	while t < n:
# 		t *= 2
# 	return t == n

# better way
def solve(n):
	return n > 0 and n & (n-1) == 0



print solve(4)