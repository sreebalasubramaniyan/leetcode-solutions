import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
       
          # Dumb Solution      
        # divisor = 1
        # flag = True
        # while flag:
        #     tot = 0
        #     for i in nums:
        #         if i % divisor == 0:
        #             tot += i / divisor
        #         else : 
        #             tot += i / divisor + 1
        #     if tot <= threshold : 
        #         return divisor
        #     divisor += 1
        
        # let us compare the threshold and len(nums)
        # nums = [1,2,5,9]
            # we can see if our divisor is 1 -> res = 17
            # div -> 2 -> res = 10
            # div -> 5 -> res = 5
            # div -> 9 -> res = 5
        # we can see if divisor increases the res increases
            # if divisor >= max(nums) res always = len(nums) <= threshold

        # in conclusion we can say divisor in range [1->max(nums)]
        # here we want smallest divisor ! yes Binay Searh 
        # 1 2 3 4 5 6 7 8 9
        # i       m       j   -> mid is divisor but we want smallest
        # i m   j             -> mid is not diviosr i = mid + 1
        #     i j             -> mid is not divisor i = mid + 1
        #     m
        #       j,m,i         -> j = mid - 1 (smallest)
        # loop end and return i
        def res(arr,d):
            tot = 0
            for i in arr:
                if i % d == 0:
                    tot += i / d
                else : 
                    tot += i / d + 1
            print(tot)
            return tot
        i = 1 ; j = max(nums) 
        while i <= j: 
            mid = (i+j) // 2
            if res(nums,mid) <= threshold : 
                j = mid - 1
            else : 
                i = mid + 1
        print(i,j)
        return i
            

        


        
