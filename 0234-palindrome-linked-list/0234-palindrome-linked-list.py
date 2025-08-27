# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        def rev(Head):
        # Using recursion leads extra space so to reduce that we 
        # use iterative method
            # 1) Recursion Method

            # if Head is None or Head.next is None :
            #     return Head
            # NewNode = rev(Head.next)
            # front = Head.next
            # front.next = Head
            # Head.next = None
            # return NewNode

            # 2) Iterative Method

            curNode = Head 
            t1 = t2 = None
            while curNode :
                t2 = curNode.next
                curNode.next = t1
                t1 = curNode
                curNode = t2
            return t1

        curNode = head 
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        NewHead = rev(slow)
        curNode = head
        while NewHead and curNode :
            if curNode.val != NewHead.val :
                return False
            curNode = curNode.next
            NewHead = NewHead.next
        return True




        # Brut Fore O(n) O(n)
        # curNode = head 
        # res = []
        # while curNode :
        #     res.append(curNode.val)
        #     curNode = curNode.next
        # return res == res[::-1]
        