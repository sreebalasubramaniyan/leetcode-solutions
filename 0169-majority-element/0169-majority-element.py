class Solution(object):
    def majorityElement(self, nums):
        # Brut Force : O(n) and O(n)
        # hashMap = {} ; n = len(nums)
        # for i in nums :
        #     hashMap[i] = hashMap.get(i,0) + 1
        # for val, count in hashMap.items() :
        #     if count > n // 2 : return  val
        # Optimal : O(n) and O(1)
        count = 0 ; n = len(nums)
        i = 0 ; res = 0
        while i < n :
            if count == 0 :
                res = nums[i]
               
            if res == nums[i] :
                count += 1
            else :
                count -= 1
            i += 1 
        return res

            