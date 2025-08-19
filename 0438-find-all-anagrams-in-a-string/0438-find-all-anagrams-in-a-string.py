class Solution(object):
    def findAnagrams(self, s, p):
        if  len(p)  > len(s) : return []

        n = len(p) ; m = len(s) ; res = []  
        hashMap = {} ;hashMap1 = {}

        for i in p : hashMap1[i] = hashMap1.get(i,0) + 1
        for i in range(n-1) : hashMap[s[i]] = hashMap.get(s[i],0) + 1

        for i in range(n-1,m) :
            hashMap[s[i]] = hashMap.get(s[i],0) + 1
            if hashMap == hashMap1 :
                res.append(i-n+1)
            hashMap[s[i-n+1]] -= 1
            if hashMap[s[i-n+1]] == 0 :
                del hashMap[s[i-n+1]]

        # if hashMap == hashMap1 : res.append(m-n)
        return res
