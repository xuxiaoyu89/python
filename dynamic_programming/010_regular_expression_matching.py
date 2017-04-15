'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
'''


# first get an example: aa : a*, aa : a.
'''
oberservation: 
. is easy, it can match any charactor
* there are two conditions
	1. s[i] == p[j-1] or p[j-1] == '.'
		1. (a)* => zero a               => dp[i][j] = dp[i][j-2]
		2. (a)* => one a  				=> dp[i][j] = dp[i][j-1]
		3. (a)* => more then one a      => dp[i][j] = dp[i-1][j]
	2. others
		zero a							=> dp[i][j-2]

dp[i][j] => s[0:i], p[0:j], i, j in (0, len+1)

dp[0][0] = True

dp[0][0~len]: if p[j] == '*' and dp[0][j-2] == true 







