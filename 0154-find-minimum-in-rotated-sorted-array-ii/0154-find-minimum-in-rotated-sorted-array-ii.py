class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # My version 
        i = 0 
        j = len(nums) - 1
        while i < j:
            mid = (i+j) // 2 
            if nums[i] == nums[j] == nums[mid]  : # This is our problem 
            # cuz we don't know whihc part to remove (left or array)
            # so we place two points one goes to left until != nums[mid] and left + 1 < i
            # same above for right

            # if the left >= right : i = right (skip left part) >= (for all are element same)
            # else : j = left (skip right part)
                left = right = mid 
                print("mid: " , mid)
                while left - 1 > i and nums[left] == nums[mid] : 
                    left -= 1
                while right  + 1 < j and nums[right] == nums[mid] : 
                    right += 1
                if nums[left] >= nums[right] : 
                    i = right
                else : 
                    j = left
                print(left,right)
            # this is our normal case in rotated array 1
                # if nums[mid] >= nums[i] and nums[mid] > nums[j] --> skip left part 
            if nums[mid] >= nums[i] and nums[mid] > nums[j] : 
                i = mid + 1 # min belongs to (mid , nums[j] ]
            else : 
                j = mid # min belongs to [ nums[i] , nums[mid] ]
            # at the end of the day we have only tow pointers then it's easy to retumr minimum
        return min(nums[i],nums[j]) 


        # test cases analysis 
            # [2, 2, 2, 0, 1]
       #  C1 : i     m     j   -> i = m != j
       #  C2 :                 -> i <= m > j -> skip left  
       #               i/m  j  -> i <= m < j -> skip right 
       #              i/m/j    -> return min(i,j) -> 0
       
        # Striver version 