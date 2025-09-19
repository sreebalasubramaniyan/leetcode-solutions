class Solution(object):
    def trap(self, nums):
        """
        hieght by height traversal
            if water add
            if bliokc pass
        we need tow ends to hold the water
            the first and last don't have their antoher ends so skip those 


   
        """ 
        n=len(nums) ; res = 0
        left,right=0,n-1
        lm,rm=nums[left],nums[right]
        while left < right:
            if lm <= rm:
                left += 1
                lm = max(lm,nums[left])
                res += lm - nums[left]
            else:
                right -= 1
                rm = max(rm,nums[right])
                res += rm - nums[right]
             

        return res 
















        #  Time : O(3n)
        #  Space : O(2n)

        # Reduced (remove left max instead keep update every time)
        # Time : O(2n)
        # Space : O(n)

        # n = len(nums)

        # # pm = nums[:]
        # # for i in range(1,n):
        # #     pm[i] = (max(pm[i],pm[i-1]))
        # sm = nums[:]
        # for i in range(n-2,-1,-1):
        #     sm[i] = max(sm[i],sm[i+1])
      
        # res = 0 ; p_max = nums[0]
        # for idx,val in enumerate( nums) :
        #     p_max = max(val,p_max)
        #     s_max = sm[idx]
        #     cur = min(p_max,s_max) - val
        #     res += cur
         





        # def solve(nums):
        #     res = []
        #     for idx,val in enumerate(nums):
        #         if val == 0 :
        #             res.append(0)
        #         elif val > 0 :
        #             res.append(1)
        #             nums[idx] -= 1
        #     return res
        # mat = []
        # times = max(nums)
        # for i in range(times):
        #     temp = solve(nums)
        #     mat.append(temp)
        # def findWater(arr):
        #     count = 0
        #     inside = False
        #     for num in arr:
        #         if num == 1:
        #             inside = True
        #         elif num == 0 and inside:
        #             count += 1
        #     i = len(arr) - 1
        #     while i >= 0 and arr[i] == 0:
        #         count -= 1
        #         i -= 1
        #     return count
        # res = 0 
        # for i in mat :
        #     res += findWater(i)
        # return res