class Solution(object):
    def minOperations(self, nums):
       
        
    # here We have to notice that the ans will be either 0 or 1
    # 0 : array already has same elements(no need of change)
    # 1 : and operation of the entire array (only once)

        return 0 if len(set(nums)) == 1 else 1