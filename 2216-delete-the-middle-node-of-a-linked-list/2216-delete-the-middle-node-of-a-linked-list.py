# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next :
            return None 
        slow = fast = head  ; prev = None
        while fast and fast.next :
            fast = fast.next.next 
            prev = slow
            slow = slow.next
        prev.next = prev.next.next
        return head