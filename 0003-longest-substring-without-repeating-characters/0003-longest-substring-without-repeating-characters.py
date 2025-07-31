class Solution(object):
    def lengthOfLongestSubstring(self, s):
    # My method 
    # the idas move the right pointer check every time wheather it is in our substring or not
    # and update our maxLen
    # and assume now j in duplicate
    # move the left pointer to first j using for loop 
    # and uppdate our substring
        # example 1
        # bacda -> j = a ; substring = bacd ; maxLen = 4
        #   i   -> i = next(a)=c  ; j = d ; maxLen = 4

        # example 2
        # pwwkew   -> j = w ; sustrign = pw ; maxLen = 2
        #   i      -> i = next(w)=w ; sustring = w ; j = k ; maxLen = 2 

        # i = 0 ; j = 0 ; n = len(s)
        # maxLen = 0
        # curS = ""
        # while j < n :
        #     if  s[j] not in curS:
        #         curS += s[j]
        #         maxLen = max(maxLen,j-i+1)
        #     else:
        #         for idx in range(i,j+1):
        #             if s[idx] == s[j]:
        #                 break
        #         i = idx + 1
        #         curS = s[i:j+1]
        #     print(curS)
        #     j += 1
        # return maxLen
       # Optimal Solution 
       # My solution works but we can optimal its run time more by using hashmap
       # the idea is moving j pointer if we s[j] not in hashmap then update with value of its index and find maxLen
       # then if it is in our hashmap then time to update our string 
       # move our pointer i to next(hash[s[j]] + 1) and update our hash[s[j]] = j ; this is our new sustring
       # reminder is even if s[j] in our hashmap we only update our substring
       # if s[j] in our substring for that s[j] >= i

        hashMap = {} ; n = len(s)
        i = j = maxLen = 0
        while j < n :
            if s[j] not in hashMap :
                maxLen = max(maxLen,j-i+1)
                
            else : 
                if hashMap[s[j]] >= i :
                    i = hashMap[s[j]] + 1
                else :   
                    maxLen = max(maxLen,j-i+1)  
            hashMap[s[j]] = j
            print(s[i:j+1])
            j += 1
        return maxLen
