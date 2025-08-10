class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def solve(nums , goal):
            if goal < 0 : return 0
            n = len(nums)
            i = j = count = curSum = 0
            while j < n :
                curSum += nums[j]
                while curSum > goal and i < n:
                    curSum -= nums[i]
                    i += 1
                count += (j-i+1)
                j += 1
            return count 
        return solve(nums,goal) - solve(nums,goal-1)

        # By Prefix Method 
        # Time : O(n) 
        # Space : O(n)    
        hashMap = {0:1} ; res = Prefix = 0 
        for i in range(len(nums)) :
            Prefix += nums[i]
            if Prefix - goal in hashMap:
                res += hashMap[Prefix-goal]
            hashMap[Prefix] = hashMap.get(Prefix,0) + 1
        return res

                
 
            

        