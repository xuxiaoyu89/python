# map, reduce, filter
reduce(lambda x, y : x^y, nums, 0) # will return the first element if len(nums) == 1


# set operations
s1 + s2
s1 - s2
s1.intersection(s2)
s1.union(s2)
s1.subset(s2) # s1 <= s2
s1.superset(s2) # s1 >= s2

s.add(key)
s.remove(key) # will raise key error if key not exist
s.discard(key) # will not raise key error if key not exist
s.clear()
s.pop() # remove and return an arbitrary element, if empty, raise error


