# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None and n == 1 or head is None:
            return None
        slow = fast = head 
        for i in range(n) :
            fast = fast.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next
        if fast is None :
            return head.next
        if slow.next is None :
            slow = None
        else : 
            slow.next = slow.next.next
        return head 