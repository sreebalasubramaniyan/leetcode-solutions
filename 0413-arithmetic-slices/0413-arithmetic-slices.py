class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if len(nums) < 3 : return 0
        i = 0 ; count = 0 ; res = 0
        while i + 1 < len(nums) :
            step = (nums[i] - nums[i+1])    
            while i + 1 < len(nums) and step == (nums[i] - nums[i+1]) :
                i += 1
                count += 1
            count += 1
            if count >= 3 : 
                nos = count  - 2
                res += nos * (nos + 1) // 2
                i -= 1
            count = 0 
            
        return res 

