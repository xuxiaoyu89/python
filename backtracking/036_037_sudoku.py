# 36: validate a sudoku


'''
idea: 
1. every 3x3 board is valid: 9 boards
2. every row is valid:       9 rows
3. every column is valid:    9 colums

so we can keep track of 27 sets
then go through each ceil in the board, for each ceil, update corresponding set
if ceil already in that set, then it is not valid

else it is valid

'''


# follow up: find the solution of a sudoku

'''
idea:
1. try every number for each empty ceil, if one is valid then, keep it
2. do this recursively.
'''

def solve(board):
    def dfs(i, j):
        if i == len(board): return result = board
        i, j = findNextEmptyCeil(i, j)
        for n in xrange(1, 10):
            if validate(board, i, j, n):
                board[i][j] = n
                dfp(i, j+1) or dfp(i+1, j)
                board[i][j] = 0
    dfs(0, 0)
    return result




'''
backtracking problem thinking process:
it is like iterate through a tree, using dfs. 
on each node, pick a valid step to its first child, then it becomes the same problem (subproblem)
then we can use recursion to solve this subproblem. 
After the first subproblem is done, then we can go to the second child, do the recursion again. 

when doing the recursion, remember to update the status and conditions of each subproblem

'''

