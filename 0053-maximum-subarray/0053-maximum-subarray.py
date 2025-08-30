class Solution(object):
    def maxSubArray(self, nums):
        
    # Brut Force : Generate all subarrays

    # Optimal : O(n) and O(1)
    # Type 1 
        curSum = 0
        maxSum = float('-inf')
        r = l = None
        for i in range(len(nums)) :
            if curSum == 0 :
                start = i
            curSum += nums[i]
            if maxSum < curSum :
                maxSum = curSum
                l = start
                r = i
            if curSum < 0 :
                curSum = 0
        print nums[l:r+1]
        return maxSum

       

    # Type 2
        # maxSum = curSum = nums[0]
        # for i in range(1,len(nums)) :
        #     curSum = max(curSum+nums[i],curSum)
        #     maxSum = max(maxSum,curSum)
        # return maxSum 