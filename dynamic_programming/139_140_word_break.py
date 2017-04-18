'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
You may assume the dictionary does not contain duplicate words.

example: 'leetcode', ['leet', 'code'], return true

'''

'''

idea:
first get the first word, let i be from [0:len(str)], 
str[0:i+1] be the first word, rest we can use recursion.
Optimization: use dp: dp[i] -> result of str[i:]
'''


def solve(s, dict):
    dp = set()
    def helper(i):
        if i in dp:
            return True
        for j in xrange(i+1, len(s)):
            if s[i:j] in dict:
                if helper(j):
                    dp.add(i)
                    return True
        return False
    helper(0)


# follow up: return all the solutions

'''
idea: instead of use a set to remember sub problems
now use a map, {i: [list of solutions]}
'''