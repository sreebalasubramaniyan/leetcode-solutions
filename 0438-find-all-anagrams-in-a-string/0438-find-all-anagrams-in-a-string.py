class Solution(object):
    def findAnagrams(self, s, p):
        hashMap1 = {}
        for i in p: 
            hashMap1[i] = hashMap1.get(i,0) + 1
        if  len(p)  > len(s) : return []
        n = len(p) ; m = len(s) ; res = [] ; hashMap = {}
        for i in range(n) : hashMap[s[i]] = hashMap.get(s[i],0) + 1
        print(hashMap1, hashMap)
        for i in range(n,m) :
            print("X : " ,  hashMap)
            if hashMap == hashMap1 :
                res.append(i-n)
            hashMap[s[i]] = hashMap.get(s[i],0) + 1
            hashMap[s[i-n]] -= 1
            if hashMap[s[i-n]] == 0 :
                del hashMap[s[i-n]]
        
        if hashMap == hashMap1 : res.append(m-n)
        return res
