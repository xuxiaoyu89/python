'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. 
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a Insert a character
b Delete a character
c Replace a character
'''

'''
find the subproblem: minimun steps to convert word1[:i] to word2[:j]
dp[i][j] = min(
            dp[i-1][j-1] + 1 # word1[i] != word2[j]
            dp[i-1][j-1] # word1[i] == word2[j]
            dp[i][j-1] + 1
            dp[i-1][j] + 1
            )

dp[0][0] = 0
dp[0][i] = i

'''

def solve(w1, w2):
    dp = array[len(w1)+1][len(w2)+1]
    # initialize
    dp[0][0]
    dp[0][j]
    dp[i][0]
    for i in xrange():
        for j in xrange():
            if w1[i] == w2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[][], dp[][], d[][])
    return dp[-1][-1]
