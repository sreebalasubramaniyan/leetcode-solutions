class Solution(object):
    def majorityElement(self, nums):
        # BrutFoce
            # hashMap frequency 
            # res ={x : x in nums h[x] > n/3}
    # Observation
        # assume it has one maj ele(a)
            # aaaaaa((n//3) + x) .......(n//3 + y)
            # (n/3+x) + n/3 + y = n ; x + y = n/3
        # if it has the tow maj ele(a,b)
            # aaaaaa(n//3+x) bbbbbb(n//3+y) ....z
            # n/3+x + n/3+y + z = n
            # x + y + z = n/3
            # z != n/3 
            # which means the nums can have only at most two(0,1,2) maj elemts
       
        
        # this is our code for maj ele n / 2 we can alter this for 
        # two elements at the same time 
        n = len(nums)
        res1 = res2 = None
        count1 = 0
        count2 = 0
        for i in nums :
            if count1 == 0 and res2 != i:
                res1 = i
                count1 = 1
            elif count2 == 0 and res1 != i:
                res2 = i 
                count2 = 1
            elif  res1 == i :
                count1 += 1
            elif  res2 == i :
                count2 += 1
            else :
                count1 -= 1 ; count2 -= 1 
               
        print res1 ,count1 
        print res2 ,count2 
        count1 = count2 = 0 
        for i in nums : 
            if i == res1 : count1 += 1
            if i == res2 : count2 += 1
        if count1 >= (n//3)+1 and count2 >= (n//3)+1:
            return list(sorted((res1,res2)))
        elif count1 >= (n//3) + 1 :
            return [res1]
        elif count2 >= (n//3) + 1:
            return [res2]
        else :
            return []
    
