# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        cur = t1 =  head  ; t2 = None
        while cur:
           cur = cur.next
           t1.next = t2
           t2 = t1
           t1 = cur
        return t2
    


        