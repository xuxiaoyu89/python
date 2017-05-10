# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
# reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
# Thus, the itinerary must begin with JFK.

'''
this is a eulerian path problem:
    for a directed graph, find a path which passes each edge exactly once.

Algorithm: Hierholzer's algorithm (which is way to hard)

we can just use basic DFS algorithm:

1) for every node, find all possible next nodes, keep this info in a map {node: [nextNodes]}
2) start from JFK, basically try every possible way.
    each time, choose one node from it's nextNodes array (in lexical order),
    and for the rest of the nodes, call the function recursively
'''


def solve(tickets):

    def dfs(start):
        if len(result) == len(tickets) + 1:
            return True
        tos = edges[start]
        for i in xrange(len(tos)):
            # delete edge from start to to
            to = tos[i]
            edges[start].pop(i)
            results.append(to)
            if dfs(to):
                return True
            edges[start].insert(to, i)
            results.pop()
        return False



    result = ['JFK']
    # first sort the tickets
    tickets.sort()
    # store the graph
    edges = defaultdict(list)
    for frm, to in tickets:
        edges[frm].append(to)
    return result



