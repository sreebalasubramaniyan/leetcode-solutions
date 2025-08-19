class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        # My Solution : O(n) and O(1)
        # No Valid
        if len(nums) < 3 : return 0
        i = 0 ; count = 0 ; res = 0
        # The Idea is 
        # we move till window is valid window 
        # once it becomes invalid then we ubdate our res cleverly by the len of our subarray ; len = count + 1
        #   example : 1 2 3 4 ; len = 4 ; n=len-2; noOfSubArrays = n*(n+1)//2 (Think of it)
        # and count becomes zero for next fresh window 
        # here is important point  we don't add i += 1 at the end of the loop
        # cuz last element of the prev subarray may be the first element of the nextSubarray (think of it)

        while i + 1 < len(nums) :
            step = (nums[i] - nums[i+1])    
            while i + 1 < len(nums) and step == (nums[i] - nums[i+1]):
                i += 1
                count += 1
            count += 1
            if count >= 3 : 
                nos = count  - 2
                res += nos * (nos + 1) // 2
                i -= 1
            count = 0  
        return res 

        # Best Solution 
        n = len(nums)
        if n < 3:
            return 0
        ans = 0
        curr = 0
        for i in range(2, n): # Check for first window so starts from 2 (third element)
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr += 1
                ans += curr # 1 + 2 + 3 + ...
            else:
                curr = 0 # for New window 
        return ans
            

