# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        carry = 0
        resLL = ListNode()
        l3 = resLL
        while l1 or l2 :
            if l1 and l2:
                Sum = l1.val + l2.val + carry
                if Sum <= 9:
                    l3.next = ListNode(Sum)
                    carry = 0
                elif Sum >= 10:
                    l3.next = ListNode(Sum-10)
                    carry = 1
                l1 = l1.next
                l2 = l2.next
                
            elif l1 :
                Sum = l1.val + carry
                if Sum <= 9:
                    l3.next = ListNode(Sum)
                    carry = 0
                elif Sum >= 10:
                    l3.next = ListNode(Sum-10)
                    carry = 1
                l1 = l1.next
                
            else :
                Sum = l2.val + carry
                if Sum <= 9:
                    l3.next = ListNode(Sum)
                    carry = 0
                elif Sum >= 10:
                    l3.next = ListNode(Sum-10)
                    carry = 1
                l2 = l2.next
            l3 = l3.next
        if carry != 0: 
            l3.next = ListNode(carry)
            l3 = l3.next
        return resLL.next