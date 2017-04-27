'''
Given an array which consists of non-negative integers and an integer m, 
you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.
'''


# thought:

'''
1. first thought, use dynamic programming.

i: number of cuts,
j: number of elements

then dp[i][j] = min(max(dp[i-1][j-k], sum(k, j))), k from [i, j]

this will have m*n*n run time complexity.

but we can do some optimization: if sum(k, j) >= the current min, then we can stop going further.



2. cleverer way, use binary search.
oberservation: the result will be sure in the range of [max(nums), sum(nums))

then we can try the middle first, m = (b + e) / 2
1. then put the numbers one by one into buckets, 
2. if curr_num + sum > middle, then put the number into the next bucket.
3. if the number of buckets are more than m, then we know we cannot make it, we need to increase m
   if less, then we know m is too large, we can make it smaller.
   if equal, we know we can still make it smaller

the time complexity will be O(n*log(sum(nums)))