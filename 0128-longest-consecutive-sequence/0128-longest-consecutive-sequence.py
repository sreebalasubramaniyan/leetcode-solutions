class Solution(object):
    def longestConsecutive(self, nums):
        # 100 4 200 1 3 2 
        # if not nums : return 0
        # hashMap = collections.Counter(nums)
        # res = 0 
        # for i in hashMap :
        #     if i-1 in hashMap or i+1 in hashMap :
        #         res += 1
            

        # return max(res,1)
        if not nums : return 0
        nums.sort() ; maxLen = float('-inf')
        i = 0 
        while i < len(nums) :
            curLen = 1
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1] :
                curLen += 1 ; 
                i += 1
                while i + 1 < len(nums) and nums[i] == nums[i+1] :
                    i += 1
            i += 1
            
            maxLen = max(maxLen,curLen)
        return maxLen




        