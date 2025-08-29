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

        # Brut Force 
            # Time  :  O(2*n) = O(n) 
            # Space : O(n)
        # if not head : return None
        # hashMap = {}
        # curNode = head
        # while curNode :
        #     newNode = ListNode(curNode.val)
        #     hashMap[curNode] = newNode
        #     curNode = curNode.next
        # print hashMap

        # curNode = head
        # newHead = ListNode()
        
        # while curNode :
        #     T = hashMap[curNode]
        #     T.next = T.random = None
        #     if curNode and curNode.next :
        #        T.next = hashMap[curNode.next]
        #     if curNode and curNode.random:
        #         T.random = hashMap[curNode.random]
        #     curNode = curNode.next
        # res = hashMap[head]
        # return res


        # Optimal 
        if not head : return None
        curNode = head
        while curNode :
            temp = curNode.next
            newNode = ListNode(curNode.val)
            curNode.next = newNode
            newNode.next = temp

            curNode = temp
        curNode = head 
        while curNode : 
            newHead = curNode.next
            if newHead :
                newHead.random = curNode.random.next if curNode.random else None
            curNode = newHead.next
        curNode = head
        res = head.next
        while curNode :
            newHead = curNode.next
            temp = newHead.next
            newHead.next =  temp.next if temp else None
            curNode.next = temp
            curNode = temp
        return res


        

