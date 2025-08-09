class Solution(object):
    def characterReplacement(self, S, k):  

          # Hashmap approach
        # brut force : O(n^2)
        # 1) generate all substring and updated maxLen if that substring satisy the condition or break 
        # 2) we want to find the maximum freq element in our current susbtring(parent) max(hashMap.values()) and remaining elements(Len(susbstrig) - maxFreq) and if the change <= k then we can update our maxLen or else break it and go to next susbtring

        # from that brut force we can reduce n ^ 2 to O(n) by our treditionnal method 
            # valid Grow, invalid Stop, shrink one step(left)
            # Change maxLen only when it's valid 
        hashMap = {}
        i = j = maxLen = maxFreq = 0
        while j < len(S) :
            hashMap[S[j]]=hashMap.get(S[j],0) + 1
            if hashMap[S[j]] > maxFreq :
                maxFreq = hashMap[S[j]]
            change = (j-i+1) - maxFreq  
            if change <= k :
                maxLen = max(maxLen,j-i+1)
            else :
                hashMap[S[i]] -= 1
                if hashMap[S[i]] == 0 :
                    del hashMap[S[i]]
                i += 1
            j += 1
            print(maxLen)
        return maxLen
        
        # My approach 
        maxLen = 0 ;n = len(S);fliped = 0  
        for target in set(S) :
            i = j = 0 
            while  j <  n : 
                cur = target
                if cur != S[j] :
                    fliped += 1
                while fliped > k:
                    if S[i] != cur :
                        fliped -= 1
                    i += 1
                maxLen = max(maxLen , j - i + 1) 
                j += 1          
            return maxLen 
  