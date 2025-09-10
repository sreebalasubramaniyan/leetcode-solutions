class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        hashMap = Counter(nums)
        # we need to sort by it's freq and if both are same then by value
        # 1st pref  : freq
        # 2nd pref  : value (if freq same)

        res = sorted(nums,key = lambda x : (hashMap[x],-x) ) 
        return res
        