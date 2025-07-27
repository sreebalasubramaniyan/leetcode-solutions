class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # First I almost i achieved the intution but I add extra not required things like (increaser)

        # The Ideas is same as I thought 
        # 1) sort the nums
            # [2,1,3,2,1,3]
            # [1,1,2,2,3,3] m-> res = 0 -> count = 0 -> m = n (assume)
            #  i       m j  -> res = 3 -> count = 1  -> m = n-2
            #    i m j      -> res = 3 + 2  -> count = 2 -> m = n-4 ... untile count < len(nums)/ 3
        # closely observe that we can see 
        # median = m1 = n - 2 ; m2 = n - 4 ; m3 = n-4 ... 
        nums.sort()
        res = 0 
        nums.sort()
        count = 0
        print(nums)
        i = 0 ; j = len(nums) - 1
        while count < len(nums) / 3 :
            
        # not required part ->  # while i < len(nums) and nums[i] == "":
                                #     i += 1
                                # while j >= 0 and nums[j] == "":
                                #     j -= 1
            res += nums[j-1]
            j -= 2
                                # print(nums[i],nums[j],nums[j-1])
                                # nums[i] = nums[j] = nums[j-1] = ""
            count+=1
        return res
            