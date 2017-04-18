# ncourses, id from 0 to n-1, given pairs of prerequests like [0, 1] 
# which means in order to take course 1, course 0 must have been token first.

# find if we can find a way to take all the courses
'''
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

def topologicalSort(n, reqs):
    s = set(range(n))
    result = []
    while reqs:
        free = s - set(map(lambda x: x[1], reqs))
        if not free:
            return ''
        result += list(free)
        reqs = filter(free.isdisjoint, reqs)
        s -= free
    return result + list(s)