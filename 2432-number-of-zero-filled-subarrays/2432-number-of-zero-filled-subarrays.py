class Solution(object):
    def zeroFilledSubarray(self, nums):

        hashMap = {} ; count = 0
        i = 0 ; res = 0
        while i < len(nums) :      
            while i < len(nums) and nums[i] == 0:
                i  += 1 
                count += 1
            res += count * (count + 1 ) // 2 
            count = 0 
            i += 1
        
        return res 


        