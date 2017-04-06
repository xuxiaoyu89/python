# do not use +

# 1 1 -> 0
# 1 0 -> 1
# 0 1 -> 1
# 0 0 -> 0


# use ^ to get different digits, 
# use & to get same digits -> get digits both is 1


# question: negative? range?

# negative integer
# -1 -> 0xFFFFFFFF
# -17 -> -(17) -> ~0x00000011 + 1-> 0xFFFFFFEE + 1 -> 0xFFFFFFEF
# 18 -> 0x000000012

# 11101111 & 00010010
def solve(n1, n2):
	while n2:
		n1, n2 = n1 ^ n2, (n1 & n2) << 1
	return n1

print solve(-17, 18)


