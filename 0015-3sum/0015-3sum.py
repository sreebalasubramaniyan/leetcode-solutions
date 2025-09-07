class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        # brut force is generate all possible non repeated three elemnts in the array and check those
        # 1st : for (i : 0 to n)
        # 2nd : for (j : i+1 to n)
        # 3rd : for (k : j+1 to n)

        # Time  : O(n^3)
        # Space : O(n)
        # hashSet = set()
        # for i in range(n) :
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 cur = [nums[i],nums[j],nums[k]]
        #                 cur.sort()
        #                 cur = tuple(cur)
        #                 hashSet.add(cur)
        # return list(hashSet)   

        # so we can reduce it n^3 to n^2 by removing of third loop and using hashMap istead
        """
        1 -2 2 1 0
        i  ... j 
        
        k = -(nums[i]+nums[j])
        if k in hashMap then it is our solution
        so we gonna add the element btwn i and j (exclusive)
        if if k in cur hashMap so i , j , k is valid soln : i + j + k = 0
        """
        hashSet = set()
        for i in range(n):
            hashMap = {}
            for j in range(i+1,n) :
                k = -1 * (nums[i] + nums[j])
                if k in hashMap :
                    cur = [nums[i],nums[j],k]
                    cur.sort()
                    cur = tuple(cur)
                    hashSet.add(cur)
                hashMap[nums[j]] = j
            
        return list(hashSet)   

