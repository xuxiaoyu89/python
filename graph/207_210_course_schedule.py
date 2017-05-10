'''
207
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, 
for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?
'''

'''
idea: detect if there is a circle in the directed graph
'''


def solve(prerequisites):
    courses = set(prerequisites)
    untaken = set(prerequisites)
    while untaken:
        take = untaken - set(lambda x:x[1], prerequisites)
        if not taken:
            return False
        untaken = untaken - take
        prerequisites = filter(take.isdisjoint, prerequisites)
    return True





'''
210
return the ordering of courses you should take to finish all courses.
'''
 
# same idea

