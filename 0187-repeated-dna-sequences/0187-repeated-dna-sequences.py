class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10 : 
            return []
        print(len(s))

        j = 9  ; hashMap = {} ; res = []
        while j < len(s) :
            cur = s[j-9:j+1]
            hashMap[cur] = hashMap.get(cur,0) + 1
            j += 1
        print(hashMap)
        
        for i , j in hashMap.items():
            if j > 1 : 
                res.append(i)
        return res

        
        