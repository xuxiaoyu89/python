'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

'''

# depth first search
# use a visited set to keep track of visited node
# use recursion to do dfs

# optimization!!!: in recursion, pass in index, instead of the suffix string

def dfs(i, j, word):
	if not word: return True
	visited.add()
	for r, c in directions:
		ni, nj are valid and ni, nj not in visited and board[ni][nj] == word[0]:
			if dfs(ni, nj, word[1:]):
				return true
	visited.discard()
