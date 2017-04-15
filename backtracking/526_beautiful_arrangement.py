'''
Suppose you have N integers from 1 to N. 
We define a beautiful arrangement as an array 
that is constructed by these N numbers successfully 
if one of the following is true for the ith position (1 ≤ i ≤ N) in this array:

1. The number at the ith position is divisible by i.
2. i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

'''

'''
1,2,3,4,5,6

same order

1-1
	2-4
	2-6
1-2
1-3
1-4
1-5


so first create a map of pairs: 
{
	1: [1,2,3,4,5,6]
	2: [2,4,6]
	3: [3,6]
}

then go throught these options one by one

use dfs(, remain)



'''




