class Solution(object):
    def romanToInt(self, s):
          
      
        ans = 0
        hashMap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L": 50,
            "C"  : 100,
            "D" : 500,
            "M" : 1000
        }
        i = res = 0
        while i +1 < len(s):
            if hashMap[s[i]] < hashMap[s[i+1]]:
                res -= hashMap[s[i]]
            else :
                res += hashMap[s[i]]
            i += 1
        res += hashMap[s[-1]]
        return res
            