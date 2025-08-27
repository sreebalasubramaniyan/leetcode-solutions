# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if not head : return head 
        head1 = head 
        head2 = head.next 
        Odd = head1
        Even = head2
        while Even and Even.next :
            Odd.next = Odd.next.next
            Even.next = Even.next.next

            Even = Even.next
            Odd = Odd.next

        Odd.next = head2 

        return head 
        
        