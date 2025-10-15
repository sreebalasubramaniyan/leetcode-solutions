from collections import deque 
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return []
        q = deque([])
        q.append(root) 
        ans = []
        count = 0
        while q :
            n = len(q)
            r = []
            if count%2 == 0 : 
                while n :
                    a = q.popleft()
                    if a:
                        r.append(a.val)
                        if a.left: q.append(a.left)
                        if a.right:q.append(a.right)
                    n-=1
            else:
                while n : 
                    a = q.pop()
                    if a :
                        r.append(a.val)
                        if a.right: q.appendleft(a.right)
                        if a.left: q.appendleft(a.left)
                    n-=1
            count += 1
            ans.append(r)
        return ans