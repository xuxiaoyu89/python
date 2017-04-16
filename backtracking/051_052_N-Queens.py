# The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
# such that no two queens attack each other.

'''
idea: 
observations: there should be exactly one queen in each row, and each column
options
1. put first queen in (0, 0), then select one from legal positions
2. put first queen in (0, 1), 
...


maintain a occupied row, column, two diaganol

'''

def solve(n):
    visitedColumns = set()
    visitedDiaganol1 = set()
    visitedDiaganol2 = set()
    result = []
    def dfs(r, prefix):
        if (r == n): result.append(prefix)
        for j in xrange(n):
            if j not in visitedColumns:
                maintain visitedColumns, visitedDiaganol1, visitedDiaganol2
                dfs(r+1, prefix + [1<<j])
                maintain visitedColumns, visitedDiaganol1, visitedDiaganol2
    dfs(0)

# Follow up: return the number of valid solutions
# even easier