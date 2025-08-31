class Solution(object):
    def getLeastFrequentDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashMap = {}
        minCount = float('inf')
        res = None

        while n > 0 :
            d = n % 10
            n //= 10
            hashMap[d] = hashMap.get(d,0) + 1
        for val,count in hashMap.items():
            if count < minCount :
                minCount = count 
                res = val
            elif count == minCount :
                res = min(res,val)
        print hashMap
        return res
        