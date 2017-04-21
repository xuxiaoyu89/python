# https://leetcode.com/problems/scramble-string/#/description

'''
thought:

first scramble, we can choose any position to seperate and swap.
so we need to check each one to verify.

say we swap s[:i], s[i:]
then s[:i] and p[:i] also need to satisfy the scramble condition.
so there come the subproblem, that is (s[:i], p[i:]) and (s[i:], p[i:]) or swap
and we can remember each one: dp[i][j], if s[i:j] can be scrambled
'''


#top-down

def solve(s, p):
    dp = {}
    def helper(b, e):
        if (b, e) in dp:
            return dp[(b, e)]
        if s[b:e] == p[b:e]:
            dp[b:e] = True
            return True
        # here we can also prune
        # sorted string, see if they are same

        for i in xrange(b+1, e):
            if (solve(b, i) and solve(i, e)) or (swap):
                dp[(b, e)] = True
        dp[(b, e)] = False
    if len(s) != len(p): return False
    return helper(0, len(s))


# bottom up
s[j:i]
dp[n][n]
for i in xrange(0, n):
    for j in xrange(i, -1, -1):
        dp[i][j] = orSum(dp[j][k] and dp[k][i]) # dp[j][k] and dp[k][i] are all known by now
return dp[n][0]