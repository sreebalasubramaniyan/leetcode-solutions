class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) ; res = -100000000000000
        i = j = 0
        while j < n :
            while j < n and nums[j] == 1 :
                j += 1
            res = max(res,j-i)
            j += 1
            i = j
        return res
        