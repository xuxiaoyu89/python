# https://leetcode.com/problems/dungeon-game/#/description
'''
knight save princess, from [0, 0] to [n, m]

each ceil can either increase health or lose health

The knight has an initial health point represented by a positive integer. 
If at any point his health point drops to 0 or below, he dies immediately.

determine knight's minimum health to reach to the princess
'''

dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j]) - ceil[i][j])