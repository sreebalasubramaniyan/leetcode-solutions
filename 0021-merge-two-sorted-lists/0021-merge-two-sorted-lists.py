# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, head1, head2):
            dummy = ListNode(0)
            c = dummy
            while head1 and head2 :
                if head1.val <= head2.val :
                    c.next = head1 
                    c = head1
                    head1 = head1.next 
                else :
                    c.next = head2
                    c = head2
                    head2  = head2.next
            if head1 : c.next = head1
            if head2 : c.next = head2
            return dummy.next
        