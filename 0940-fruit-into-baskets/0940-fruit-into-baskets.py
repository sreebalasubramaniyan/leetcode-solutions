class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        # res = 0
        # for start in range(len(fruits)):
        #     bas1 = bas2 = None
        #     cur = 0
        #     for j in range(start,len(fruits)):
        #         i = fruits[j]
        #         if bas1 == None :
        #             bas1 = i
        #         elif bas2 == None :
        #             bas2 = i
        #         if i == bas1:
        #             cur += 1
        #         elif i == bas2 :
        #             cur += 1
        #         else : 
        #             break
        #     res = max(res,cur)
        # return res
    


    # maximum len sub array having only two type of elements

        # bas1 = bas2 = None ; n = len(fruits)
        # res = 0
        # i = j = 0
        # cur = 0
        # while j < n:
        #     i = j
        #     if bas1 == None :
        #         bas1 = fruits[j]
        #     elif bas2 == None and fruits[j] != bas1:
        #         bas2 = fruits[j]

        #     if bas1 == fruits[j] and bas1 != None:
        #         cur += 1
        #     elif bas2 == fruits[j] and bas2 != None:
        #         cur += 1
        #     else :
        #         # print("Hi")
        #         # idx = j - 1
        #         # cur = 2 
        #         # while idx - 1 >=0 and fruits[idx-1] == fruits[j-1] :
        #         #     cur += 1
        #         #     idx -= 1
        #         # bas1 = fruits[j-1]
        #         # bas2 = fruits[j]
        #         cur = 1
        #         if i-1 >= 0 and fruits[i-1] == bas1 :
        #             bas2 = fruits[j]
        #             i -= 1
        #             cur += 1

        #         elif i-1 >=0 and fruits[i-1] == bas2 :
        #             bas1 = fruits[j]
        #             cur += 1
        #             i -=1 
        #         continue
                
            
        #     j += 1

        d = dict()
        i = j = maxLen = 0 
        while j < len(fruits) : 
            right = fruits[j]                   
            temp = d.get(right,0) + 1
            d[right] = temp
            if len(d) > 2 :
                left = fruits[i]
                d[left] -=1 
                if d[left] == 0 :
                    del d[left]
                i += 1
            if len(d) <= 2 : 
                maxLen = max(maxLen,j-i+1)
            j+= 1
                

        return maxLen

            