# ncourses, id from 0 to n-1, given pairs of prerequests like [0, 1] 
# which means in order to take course 1, course 0 must have been token first.

# find if we can find a way to take all the courses





'''
BFS way

observation: all courses and prerequisites form a directed graph.
we cannot take a course before it's prerequisites has been token.

so we can take the ones which do not have prerequisites,

then update the graph -> 
    remove the node (chose courses) and 
    the edge (the prerequisition where chosen course is required)

then take the ones which do not have prerequisites again in a loop

if there is a loop in the directed graph, then there is no such way to take all the courses
and in this case, there will be no free courses(courses that have no prerequisites)

'''

def topologicalSort(n, prerequisites):
    s = set(range(n))
    result = []
    while prerequisites:
        free = s - set(map(lambda x: x[1], prerequisites))
        if not free:
            return ''
        result += list(free)
        prerequisites = filter(free.isdisjoint, prerequisites)
        s -= free
    return result + list(s)



'''
DFS way

from a arbitrary node, visit all the nodes it can reach, put all these nodes into an array (by branch), mark visited
iterate all unvisited node, run the same dfs algorithm, and put later results in front of the previous results.

'''

# note: this method only works if there is no cycle.


from collections import defaultdict
def solve(n, prerequisites):
    def dfs(n):
        visited.add(n)
        for nxt in m[n]:
            if nxt not in visited:
                dfs(nxt)
        result.insert(0, n)
        return

    m = defaultdict(list)
    for o, i in prerequisites:
        m[i].append(o)
    visited = set()
    result = []
    for i in xrange(n):
        if i not in visited:
            dfs(i)
    return result

print solve(2, [[1, 0]])
























