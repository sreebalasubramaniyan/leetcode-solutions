class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        n = len(nums)
        k = k % n
        if k == 0:
            return
        
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k,n-1)
        reverse(nums, 0,n-1)
        return nums
        k %= len(nums) ; n = len(nums)
        temp = []
        for i in range(n-k,n) :
            temp.append(nums[i])
        idx = n - k  - 1
        while idx >= 0 :
            nums[idx+k] = nums[idx]
            idx -= 1
        for i in range(k):
            nums[i]= temp[i]
        return nums




