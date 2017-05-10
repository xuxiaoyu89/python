# detect cycle in a directed graph

'''
idea:
    use DFS to travel through all the nodes, and mark the one visited. if we travel to a visited one 

'''

from collections import defaultdict
def solve(n, prerequisites):
    visited, stack, m = set(), set(), defaultdict(list)
    for i, o in prerequisites:
        m[i].append(o)

    def dfs(i):
        if i in visited: return True
        if i in stack: return False
        stack.add(i)
        for o in m[i]:
            if not dfs(o):
                return False
        stack.remove(i)
        return True

    for i in xrange(n):
        if i not in visited:
            if not dfs(i):
                return False
    return True



print solve(3, [[0,1], [1,2], [2,1]])

