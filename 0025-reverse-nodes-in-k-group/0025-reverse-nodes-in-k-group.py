# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def rev(H) :
            if not H or not H.next :
                return H
            newHead = rev(H.next)
            front = H.next
            front.next = H
            H.next = None
            return newHead
        
        resLL = ListNode()
        R  = resLL
        fast = slow = head

        while fast and fast.next :
            temp = k
            while temp > 1 and fast.next :
                temp -= 1
                fast = fast.next
            if temp == 1 :
                print slow.val , fast.val
                X = fast.next
                fast.next = None
                R.next = rev(slow)
                R = slow
                fast = X
                slow = fast 
            else :
                break
        print slow
        if slow :
            R.next = slow
        return resLL.next


        




        