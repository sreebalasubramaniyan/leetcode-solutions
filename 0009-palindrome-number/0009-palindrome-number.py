class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp1 = temp2 = x 
        res = 0
        digit = 0
        while temp1 > 0:
            temp1 //= 10
            digit += 1
        print(digit)
        i = 1
        while temp2 > 0 : 
            d = temp2 % 10
            res = res * 10 + d
            temp2 //= 10
        print(res)
        return res == x

        