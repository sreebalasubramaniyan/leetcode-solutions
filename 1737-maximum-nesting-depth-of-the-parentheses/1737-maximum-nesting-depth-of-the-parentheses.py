class Solution(object):
    def maxDepth(self, s):
        """

        (()(()))

        () (()) ((()))
        ()(())((()()))


        """

        # here insead of using stack we can just go with the counter

        # stack = []
        count = 0
        ans = float('-inf')
        for i in s :
            if i == "(":
                # stack.append(i)
                count += 1
            elif i == ")" :
                # cur = len(stack)
                ans = max(ans,count)
                # stack.pop()
                count-=1
        if ans == float('-inf') : return 0
        return ans