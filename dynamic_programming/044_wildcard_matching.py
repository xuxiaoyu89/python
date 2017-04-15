'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
'''

'''
dp

p[i], s[j]

1. p[i] == s[j] or p[i] == ? => dp[i][j] = dp[i-1][j-1]; i, j ++
2. p[i] != s[j] => dp[i][j] = False
3. p[i] == '*' => 
	1. not use * => dp[i-1][j]
	2. use * => dp[i][j-1]


p[0][0] = True
p[0][j] = False

p[i][0] = True before something not *

'''


'''
backtracking
keep the latest * (b) match to position a in s 

1. s[i] == p[j] or p[j] == '?': i, j ++
2. p[j] == '*': a = i, b=j, i += 1, j += 1, 
3. else, doesn't match :
	1. if no *, return false
	2. if has *, go back to last *
		a += 1, i = a
		1. if i >= len(s):
			break
		2. else:
			j = b + 1
return i == len(s) and j == len(j)
'''

