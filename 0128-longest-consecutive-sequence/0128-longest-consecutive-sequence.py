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
        # if not nums : return 0
        # nums.sort() ; maxLen = float('-inf')
# Type 1
        # i = 0 
        # while i < le(nums) :
        #     curLen = 1
        #     while i + 1 < len(nums) and nums[i] + 1 == nums[i+1] :
        #         curLen += 1 ; 
        #         i += 1
        #         while i + 1 < len(nums) and nums[i] == nums[i+1] :
        #             i += 1
        #     i += 1

# Type 2 
        # prev = nums[0] ; curLen = 1 ; maxLen = float('-inf')
        # for i in range(1,len(nums)) :
        #     if nums[i] == prev : continue
        #     if prev + 1 == nums[i] : curLen += 1
        #     else :curLen = 1
        #     prev = nums[i]
        #     maxLen = max(maxLen,curLen)
        # return max(maxLen,curLen)

        # Optimal 
        if not nums : return 0
        hashSet = set(nums)
        curLen = 0  ; maxLen = float('-inf')
        for i in hashSet :
            cur = i
            if cur - 1 not in hashSet :
                curLen = 1
                while cur + 1 in hashSet :
                    curLen += 1
                    cur += 1
            maxLen = max(maxLen,curLen)
        return maxLen





        