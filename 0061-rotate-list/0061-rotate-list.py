# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head  :
            return None
        def Len(Head) :
            curNode = Head ; count = 0
            while curNode :
                curNode = curNode.next
                count += 1
            return count
        k = k % Len(head)

        slow = fast = head
        for i in range(k) :
            fast = fast.next
        while fast and fast.next :
            fast = fast.next
            slow = slow.next
        fast.next = head
        head = slow.next 
        slow.next = None
         
        return head