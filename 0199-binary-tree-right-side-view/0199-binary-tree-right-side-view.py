# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        q = deque([root])
        ans = []
        while q :
            r = []
            n = len(q)
            while n :
                n -= 1
                a = q.popleft()
                if a :
                    r.append(a.val)
                    if a.left : q.append(a.left) 
                    if a.right : q.append(a.right) 
            if r : ans.append(r[-1])
        return ans