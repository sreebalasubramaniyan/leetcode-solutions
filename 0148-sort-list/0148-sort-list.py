class Solution(object):
    def sortList(self, head): 
    # Optimal 
        # Time  : O(n*log n) 
        # Space : O(1)
        def Merge(leftHead,rightHead) :
            curLL = ListNode(0)
            l1 = leftHead
            l2 = rightHead
            curNode = curLL
            while l1 or  l2 :
                if l1 and l2 :
                    if l1.val <= l2.val :
                        curNode.next = l1
                        l1 = l1.next
                    else:
                        curNode.next = l2
                        l2 = l2.next
                elif  l1 :
                    curNode.next = l1
                    l1 = l1.next
                else :
                    curNode.next = l2
                    l2 = l2.next
                curNode = curNode.next
            return curLL.next
       
        def MergeSort(Head) :
            if not Head or not Head.next :
                return Head
            slow = fast = Head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next 
                slow = slow.next
            mid = slow
            leftHead = Head
            rightHead = mid.next
            mid.next = None
            leftHead = MergeSort(leftHead)
            rightHead = MergeSort(rightHead)
            res = Merge(leftHead, rightHead)
            return res

        
        head = MergeSort(head)
        return head
        
        
        
    # Brut Force
        # Time  : O(n*log n)
        # Space : O(n) 
        # nums = []
        # curNode = head 
        # while curNode :
        #     nums.append(curNode.val)
        #     curNode = curNode.next
        # nums = sorted(nums)
        # curNode = head ; count = 0 
        # while curNode :
        #     curNode.val = nums[count]
        #     count += 1
        #     curNode = curNode.next
        # return head 

        