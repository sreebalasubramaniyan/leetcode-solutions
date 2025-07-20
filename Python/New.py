

# 1351. Count Negative Numbers in a Sorted Matrix

1) Question
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

2) Clue or Key Point : Sorted in non-increasing order and we have return the single value
which is looks like binary search

3) Pattern : return J method -> here we want  a first negative numbers pos
cuz after that the rest of numbers should be negative and just add res += len(row) - j

4) Complexity
Time  : O(mlog(n))
Space : O(1)

5) Code

class Solution(object):
def countNegatives(self, grid):
"""
:type grid: List[List[int]]
:rtype: int
"""

res = 0
for row in grid:
i = 0
j = len(row) - 1
while i<j:
mid = (i+j) // 2
if row[mid] >= 0:
i = mid + 1
else :
j = mid
if row[j] < 0 :
res += len(row) - j
return res


