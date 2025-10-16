# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def search(node,val):
            if not node :
                return False
            if node.val < val :
                return search(node.right,val)
            elif node.val > val :
                return search(node.left,val)
            else:
                return node
        ans = search(root,val)
        return ans if ans else None