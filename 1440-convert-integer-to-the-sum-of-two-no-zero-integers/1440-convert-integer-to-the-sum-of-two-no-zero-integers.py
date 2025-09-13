class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        
        n is even
        n/2   n/2
        101
        100
        99
        2

        10107
        999 + 100
        988 + 111
        9996 + 111
        a = n - b

        if n > 10 
        find maximum three 99 number and find ans
        """
        if n < 10:
            if n & 1 :
                return [n//2+1,n//2]
            else:
                return [n//2,n//2]
        
        def isZero(n):
            while n :
                d = n % 10
                if not d : return True
                n //= 10
            return False
        temp = n
        dig = 0
        while temp :
            temp //= 10 
            dig += 1
        dig -= 1
        nine = int('9' * dig)
        a = nine
        b = n - nine
        print a ,b
        if not isZero(b) :
           return [b,a]
        else:
            temp = b
            B = 0
            count = 0
            while temp :
                d = temp % 10
                if not d :
                    B = B + pow(10,count)
                temp //= 10
                count += 1
        a = a - B
        b = b + B
        print (a,b)
        if not isZero(a) and not isZero(b) :
            return [b,a]
        print B

        
        

        