# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curNode = temp = head 
        while curNode :
            temp = curNode
            while temp and temp.next and temp.val == temp.next.val :
                temp = temp.next
            curNode.next = temp.next
            curNode = curNode.next

        return head 
        