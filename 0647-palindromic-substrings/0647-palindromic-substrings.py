class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        babbc
        """

        n = len(s)
        ans = 0
        middle = 0
        while middle  < n:
        # odd length
            left = middle 
            right = middle
            while left >=0 and right < n and s[left] == s[right] :
                left -= 1
                right += 1
                ans += 1
        # even length
            left = middle
            right = middle + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right +=  1
                ans += 1
            middle += 1
        return ans
