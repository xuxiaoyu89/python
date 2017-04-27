'''
idea: 
maintain a increasing subsequence, 
for the next number, 
1. if it is larger than the right-most (largest) one in the current sequence,
    then add to the end
2. else: find the first element that is larger then it, and replace it. 
    The idea here is to make the right-most one as small as possible

'''
import bisect
def solve(nums):
    result = []
    for n in nums:
        if not result or n >= result[-1]: 
            result.append(n)
            continue
        # find the smallest one that is larger then n
        i = bisect.bisect_left(result, n)
        result[i] = n

    return result



