class Solution(object):
    def findContentChildren(self, g, s):
        """
        I want to give a cookie to minimum diff child
        diff(s[j]-g[i]) shold be minimum
        
        ans = 0 to len(s)

        cookie : 4 5 8
        childe : 6 3 2

        """
        g.sort(reverse = True)
        s.sort() ; ans = 0
        for i in s:
            if g and g[-1] <= i:
                ans += 1
                g.pop()
        return ans
        