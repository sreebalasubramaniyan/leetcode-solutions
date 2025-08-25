# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):

        # Time  : O(n) 
        # Space : O(n)
        # hashSet = set()
        # curNode = head
        # while curNode :
        #     if curNode in hashSet :
        #         return curNode 
        #     hashSet.add(curNode)
        #     curNode = curNode.next
        # return None 
        
        # Time  : O(n)
        # Space : O(1)

        fast = slow = head 
        while  fast and fast.next :
            fast = fast.next.next
            slow = slow.next
            if fast == slow :
                slow = head
                while slow != fast :
                    slow = slow.next 
                    fast = fast.next 
                return slow
        return None 

