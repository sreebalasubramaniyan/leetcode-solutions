class Solution(object):
    def maxFreqSum(self, s):
        v = {}
        c = {}
        for i in s :
            if i.lower() in "aeiou":
                v[i.lower()] = v.get(i.lower(),0) + 1
            else:
                c[i.lower()] = c.get(i.lower(),0) + 1
        if c and v : return max(c.values()) + max(v.values())
        if c : return max(c.values())
        if v : return max(v.values())
        return 0