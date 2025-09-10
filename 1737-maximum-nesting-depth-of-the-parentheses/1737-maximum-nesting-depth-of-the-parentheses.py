class Solution(object):
    def maxDepth(self, s):
        """

        (()(()))

        () (()) ((()))
        ()(())((()()))


        """

        # S = "" 
        # for i in s :
        #     if i == "(" or i==")" :
        #         S += i
        # if not S :  return 0
        stack = []
        ans = float('-inf')
        for i in s :
            if i == "(":
                stack.append(i)
            elif i == ")" :
                cur = len(stack)
                ans = max(ans,cur)
                stack.pop()
        if ans == float('-inf') : return 0
        return ans