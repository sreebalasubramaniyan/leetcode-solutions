"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head : return None
        hashMap = {}
        curNode = head
        while curNode :
            newNode = ListNode(curNode.val)
            hashMap[curNode] = newNode
            curNode = curNode.next
        print hashMap

        curNode = head
        newHead = ListNode()
        
        while curNode :
            T = hashMap[curNode]
            T.next = T.random = None
            if curNode and curNode.next :
               T.next = hashMap[curNode.next]
            if curNode and curNode.random:
                T.random = hashMap[curNode.random]
            curNode = curNode.next
        res = hashMap[head]
        return res
        