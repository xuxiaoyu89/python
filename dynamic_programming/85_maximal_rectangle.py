# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest rectangle containing only 1's and return its area.


'''
soultion 1:

borrow idea from leetcode 84. Largest Rectangle in Histogram

use stack to get the largest rectangle for each row.
'''



'''
Solution 2:
kind of like dp
iterate through the matrix, for each element e(i, j), 
calculate the max area, using height as the current consecutive 1s in this column so far.
using width as the max width possible in the rows where e(i, j) == 1



