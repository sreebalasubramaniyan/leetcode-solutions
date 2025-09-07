class Solution(object):
    def minOperations(self, nums):
       
        
    # here We have to notice that the ans will be either 0 or 1
    # 0 : array already has same elements(no need of change)
    # 1 : and operation of the entire array (only once)

    # nums = [a,b,c,...,x,y,z] 
    # we always choosing the entire array as a subarray
    # so at the end we get any answer that does not matter
    # and simply we replace the all elements with that ans
    # so no operation will be alwasy will be 1

    # if the all elements are already same means the operation will be 0(no need) 

        return 0 if len(set(nums)) == 1 else 1