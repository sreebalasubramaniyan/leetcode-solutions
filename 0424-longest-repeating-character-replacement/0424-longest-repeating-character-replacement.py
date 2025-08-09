class Solution(object):
    def characterReplacement(self, S, k):  
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

class Solution(object):
    def characterReplacement(self, S, k):
        maxLen = 0
        n = len(S)

        # Try making the string all of each possible letter
        for target in set(S):
            i = j = 0
            flips = 0
            while j < n:
                if S[j] != target:
                    flips += 1
                while flips > k:
                    if S[i] != target:
                        flips -= 1
                    i += 1
                maxLen = max(maxLen, j - i + 1)
                j += 1
        return maxLen
