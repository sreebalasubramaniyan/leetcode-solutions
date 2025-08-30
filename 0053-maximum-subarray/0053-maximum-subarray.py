class Solution(object):
    def maxSubArray(self, nums):
        
    # Brut Force : Generate all subarrays

    # Optimal : O(n) and O(1)
        curSum = 0
        maxSum = float('-inf')
        for i in nums :
            curSum += i 
            if curSum < 0 :
                curSum = 0
                if i > maxSum :
                    maxSum = i
            else :
                maxSum = max(maxSum,curSum) 
        return maxSum