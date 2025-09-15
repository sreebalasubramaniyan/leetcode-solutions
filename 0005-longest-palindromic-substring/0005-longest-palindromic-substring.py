class Solution(object):
    def longestPalindrome(self, s):
        """
        Brut Force : 
            n - outer
                n -inner
                    n - form string(worst)
            over all O(n^3)

        Better or optimal
            for each letter find the maximum pali that the letter can make
            so assume the letter as mid ele of pali and find the maxi pali for each letter
            and find the overall maximum from the each leeter's maxi pali

            visual
              s=babad
                b-> b
                a->  bab
                a->  aba
                d->  d
            here you can see that every pali(max) is odd length so we don't consider even len
            but ans may be even len so we have to handle this edge case

           s = aabbaacdefggeeiijj
            

                


        """


        n = len(s)
        res_i = 0
        middle = 0
        maxLen = 0

        while middle  < n:
        # odd length
            left = middle 
            right = middle
            while left >=0 and right < n and s[left] == s[right] :
                left -= 1
                right += 1
            left += 1 ; right -= 1
            curLen = right - left + 1
            if curLen > maxLen :
                res_i = left ; maxLen = curLen   
        # even length
            left = middle
            right = middle + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right +=  1
            left += 1 ; right -= 1
            curLen = right - left + 1
            if curLen > maxLen :
                res_i = left ; maxLen = curLen   
            middle += 1
        ans = s[res_i:res_i+maxLen]
        return ans


        res = None
        maxLen = -1
        for i in range(len(s)):
            for j in range(i,len(s)):
                cur = s[i:j+1]
                if cur == cur[::-1] :
                    if maxLen < len(cur):
                        maxLen = len(cur)
                        res = cur
        return res
        