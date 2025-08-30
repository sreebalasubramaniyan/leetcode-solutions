class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
#  Non Relative Order 
        # i = 0 
        # j = len(nums) - 1
        # while i < j :
        #     while i < j and nums[i] != 0 :
        #         i += 1
        #     while i < j and nums[j] == 0 :
        #         j -= 1
        #     print nums[i] , nums[j]
        #     nums[i],nums[j] = nums[j],nums[i]
        #     print nums[i] , nums[j]
        #     i+=1 ; j -=1
        # return nums
#   Relative Order 

        # i = 0 
        # while i < len(nums) :
        #     if nums[i] == 0:
        #         j = i 
        #         while j  < len(nums)  and  nums[j] == 0 :
        #             j += 1
        #         if i < len(nums) and j < len(nums) :
        #             nums[i],nums[j] = nums[j],nums[i]
        #     i += 1

        # 0 1 0 3 12 
        # 1 0 0 3 12
        # 1 3 0 0 12 
        # 1 3 12 0 0 

        i = j = 0
        while j  < len(nums) :
            while j < len(nums) and nums[j] == 0 :
                j += 1 
            if j < len(nums) : 
                nums[i] , nums[j] = nums[j] , nums[i]
            i += 1
            j += 1

