class Solution(object):
    def minWindow(self, s, t):
        hashMap = {}
        for i in t :
            hashMap[i] = hashMap.get(i,0) + 1
        k = j = 0 ; minLen = 100000000 ; Idx = -1
        if len(s) < len(t) : return ""
        count = 0
        while j < len(s) :
            while j < len(s) and count != len(t):
                if s[j] in hashMap:
                    if hashMap[s[j]] > 0 :
                        count += 1
                    hashMap[s[j]] -= 1
                else:
                    hashMap[s[j]] = -1
                j += 1
            while k < j and count == len(t):
                if j - k < minLen :
                    minLen = j -k
                    Idx = k
                hashMap[s[k]] += 1
                if hashMap[s[k]] > 0:
                    count -= 1
                k += 1
            print hashMap
        
        if minLen == 100000000 : return ""
        if minLen < len(t) : return ""
        return s[Idx:Idx+minLen]
          
                
        

        
                
        