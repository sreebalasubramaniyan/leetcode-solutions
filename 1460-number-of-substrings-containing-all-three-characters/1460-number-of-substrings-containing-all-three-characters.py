class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        a = b = c = -1 ; res = 0
        for i in range(len(s)) :
            if s[i] =='a': a = i
            if s[i] =='b': b = i
            if s[i] =='c': c = i
            if a!=-1 and b!=-1 and c!=-1:
                res += min(a,b,c) + 1
        return res

        # res = 0 
        # hashMap = {}
        # index = []
        # for i in range(len(s)) :
        #     if s[i] not  in hashMap:
        #         hashMap[s[i]]  = i
        # if len(hashMap) != 3 : return 0
        # maxIdx = 0 
        # for i in hashMap:
        #     if hashMap[i] > maxIdx :maxIdx = hashMap[i]
        # i = maxIdx
        # if i == len(s) - 1:
        #     k = 0
        #     while k < len(s) : 
        #         if 'a' in s[k:] and 'b' in s[k:] and 'c' in s[k:]:
        #             k += 1
        #         else :
        #             k -= 1
        #             break
        #     return k+1

        # i = maxIdx + 1
        # while i < len(s) :
        #     res += hashMap[s[i]] + 1 + 1
        #     i+=1
        # return res + 1
            

