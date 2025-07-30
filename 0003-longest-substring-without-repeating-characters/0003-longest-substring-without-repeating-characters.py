class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0 ; j = 0 ; n = len(s)
        maxLen = 0
        curS = ""
        while j < n :


            if  s[j] not in curS:
                curS += s[j]
                maxLen = max(maxLen,j-i+1)
            else:
                for idx in range(i,j+1):
                    if s[idx] == s[j]:
                        break
                i = idx + 1
                curS = s[i:j+1]
            print(curS)
            j += 1
        return maxLen
        # S  r  e  e
        # ij         -> C ="S"
