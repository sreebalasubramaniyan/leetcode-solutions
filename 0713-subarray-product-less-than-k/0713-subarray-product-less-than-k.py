class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        i = res = 0
        j = 0
        curPr = 1
        if k == 0 : return 0
        while j  < len(nums):
            curPr *= nums[j]
            while i < j and curPr >= k :
                curPr /= nums[i]
                i += 1
            if curPr < k :
                res += j - i + 1
            j += 1
            
        return res
        