class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0 
        j = len(nums) - 1
        while i < j:
            mid = (i+j) // 2 
            if nums[i] == nums[j] == nums[mid]  :
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
            if nums[mid] >= nums[i] and nums[mid] > nums[j] : 
                i = mid + 1
            else : 
                j = mid
        return min(nums[i],nums[j])