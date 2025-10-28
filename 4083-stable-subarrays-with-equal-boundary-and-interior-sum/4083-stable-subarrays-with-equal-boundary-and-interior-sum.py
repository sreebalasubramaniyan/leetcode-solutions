class Solution(object):
    def countStableSubarrays(self, nums):
        ans = 0 
        N = len(nums)
        map = collections.defaultdict(int)
        prefix = [nums[0]]
        for i in range(1,N):
            prefix.append(prefix[-1]+nums[i])
        for j in range(N-1,-1,-1):
            ans += map[(nums[j],prefix[j]+2*nums[j])]
            if j + 1 < N:
                map[(nums[j+1],prefix[j+1])] += 1
        return ans