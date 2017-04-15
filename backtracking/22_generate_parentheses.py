'''
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.
'''

'''
thoughts
in the process of building a valid combination, we have i '(' and j ')'
then we can continue to add '(' if i < n
we can continue to add ')' if i > j

if i == j == n: we got a valid combination
'''

# can use recursion.

result = []
def solve(n, i, j, prev):
	if i == j == n:
		result += prev
	if i > j:
		solve(n, i, j+1, prev+')')
	if i < n:
		solve(n, i+1, j, prev+'(')


