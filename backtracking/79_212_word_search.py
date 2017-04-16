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


# follow up: 212: word search 2

# Given a 2D board and a list of words from the dictionary, find all words in the board.

# idea:
'''
1. build a trie with the words from the dictionary
2. iterate each c in the board, do dfs: 
    for each neighbour, 
        if it exists in the subtree, then dfs recursion,
        else: then we can trunk the whole subtree
'''

def buildTrie(dict)
    return root
def solve(board, dict):
    result = []
    def dfs(i, j, root):
        c = dict[board[i][j]]
        if '#' in root: result.append(root['#'])
        if c in root:
            for ni, nj in neighbours:
                dfs(ni, nj, root[c]) 
        else:
            return

    trie = buildTrie(dict)
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            dfs(i, j, board, trie)

















