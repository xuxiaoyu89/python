# get ith bit of a number
def get(num, i):
	mask = 1 << i
	return 1 if num & mask else 0

# clear the ith bit of a number
def clear(num, i):
	mask = ~(1 << i)
	return num & mask

def set(num, i):
	mask = 1 << i
	return num | mask

n ^ (n-1) == 0 # n is power of 2

n ^ n = 0
n & n = n
n | n = n

n & 1s => n
n | 1s => 1s
n ^ 1s => ~n

n & 0s => 0s
n | 0s => n
n ^ 0s => n

# 32 bit signed integer:
max = 2**31 - 1 # 0x7FFFFFFF
min = -2**31    # 0x80000000 <= ~0x80000000 + 1

# how is a negative number presented in binary?
a = -25 # what is the binary representation of a?
a == ~25 + 1 # 


