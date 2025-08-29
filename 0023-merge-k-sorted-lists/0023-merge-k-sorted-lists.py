# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        if not lists :
            return None
        if len(lists) == 1 :
            return lists[0]
        def Sort(head1 , head2) :
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

        # Brut Force 
            # Time  : 2N + 3N + 4N upto k times -> N * K ^ 2  
            # Space : O(1) 
        # head = lists[0]
        # for i in range(1,len(lists)) :
        #     curHead = lists[i]
        #     head = Sort(head,curHead)
        

        # Optimal 
        res = ListNode()
        R = res
        MinHeap = []
        for i in lists:
            if i :
                heapq.heappush(MinHeap,[i.val,i]) 
        print MinHeap
        while MinHeap :
            curVal = heapq.heappop(MinHeap)
            R.next = ListNode(curVal[0])
            R = R.next
            if curVal[1] and curVal[1].next :
                heapq.heappush(MinHeap,[curVal[1].next.val,curVal[1].next])
        return res.next
        
       























