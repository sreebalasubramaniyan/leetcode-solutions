class Solution(object):
    def merge(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [nums[0]] 
        for rng in nums :
            if rng[0] <= res[-1][1] : 
                if rng[1] > res[-1][1]:
                    res[-1] = [res[-1][0],rng[1]] 
            else :
                res.append(rng)
        return (res)