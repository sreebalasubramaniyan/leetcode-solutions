class Solution(object):
    def minWindow(self, s, t):


        # 1) Create a hashMap of t (frequency counter)
        # 2) traverse in s, if s[j] in hashMap and freq[s[j]] > 0 (preinserted)
        # 3) that is our req char so increase count += 1
        # 4) if count == len(t) then that is our valid window 
        # 5) here we break that and check weather can we shrink the window cuz we need smallest substring
        # 6) so shrink the window from left and if freq[s[i]] > 0 then count -= 1
        # 7) after that if minLen < j - i then that is our new smallest valid window
        # 8) i = startIndex & minLen = j - i
        # 9) at the end check some edge cases and return the window s[Idx : Idx + minLen]

        hashMap = {}
        for i in t :
            hashMap[i] = hashMap.get(i,0) + 1
        k = j = 0 ; minLen = 100000000 ; Idx = -1
        count = 0
        if len(s) < len(t) : return ""

        while j < len(s) :
            while j < len(s) and count != len(t): # Grow Up to valid
                if s[j] in hashMap:
                    if hashMap[s[j]] > 0 :
                        count += 1
                    hashMap[s[j]] -= 1
                else:
                    hashMap[s[j]] = -1
                j += 1
            while k < j and count == len(t): # Shrink Up to Valid
                if j - k < minLen : # then that is our new small substring 
                    minLen = j -k
                    Idx = k 
                hashMap[s[k]] += 1
                if hashMap[s[k]] > 0: # this is the one of the charecters that in t
                    count -= 1
                k += 1

        # EdgeCases
        if minLen == 100000000 : return ""
        if minLen < len(t) : return ""
        # Result
        return s[Idx:Idx+minLen]
          
                
        

        
                
        