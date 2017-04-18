# 290: easy

# 291: Given a pattern and a string str, find if str follows the same pattern.
# pattern = "abab", str = "redblueredblue" should return true.


'''
idea:
for a character in pattern, choose the prefix of the string as its pattern
then do this recursively to find if there is a match
1. if there is a match, return True
2. if there is no match, choose another prefix of the string as its pattern

'''


def solve(p, s):
    dic = {}
    def dfs(i, j):
        if i == len(p): return True
        if j == len(s): return False
        if (p[i]) in dic:
            pattern = dic[p[i]]
            return dfs(i+1, j+len(pattern))
        for k in xrange(1, len(s)-j):
            dic[p[i]] = s[j, j+k]
            if dfs(i+1, j+k):
                return True
        return False

    dfs(0, 0)

