class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1 :
            if k == nums[0]:
                return 1
            else :
                return 0
        # nums = [0,0,0,0,0] ; k = 0
        #       1 3 3 6 10
        i = j = res = Prefix = 0
        hashMap = {0:1}
        while j < len(nums) :
            Prefix += nums[j]
            
            # if Prefix >= K : [Prefix] = [X-K] + [K] 
            # K = SumOfSome any subarray
            # here is main thing , no of subarrays is not necessarily = 1
            # so we count all possible K (hashMap)
            if Prefix - k  in hashMap :
                res += hashMap[Prefix-k]
            hashMap[Prefix] = hashMap.get(Prefix,0) + 1
            j += 1
        
        return res