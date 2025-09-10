class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
     1. (()()) (())
        ()()    ()
        ()()()
    2. (()()) (()) (()(()))
        ()()   ()   ()(())
        ()()()()(())
        
    3.  ()()   
        
        
       1) n = len(s)
        Time : O(2n)
        Space: O(2n)
        
        2)  n = len(s)
        Time : O(n)
        Space: O(2*n)

        2)  n = len(s)
        Time : O(n)
        Space: O(n) just for ans


        
        """
    # Soln 3 Optimal

        count = 0
        res = ""
        for i in range(len(s)):
            if s[i] == "(" :
                if count > 0 :
                    res += s[i]
                count += 1
            else :
                count -= 1
                if count > 0 :
                    res += s[i]
        return res

    # Soln 2 better
        stack = []
        left = 0 
        ans = ""
        for i in range(len(s)):
            if stack and not(len(stack) == 1 and s[i] == ")"):
                ans += s[i]
            if s[i] == "(" :
                stack.append(s[i])
            elif s[i] ==")":
                stack.pop() # s is the valid paranthesis str
        return (ans)  


    # soln 1 brut force
        stack = []
        left = 0 
        res = set()
        for i in range(len(s)):
            if s[i] == "(" :
                stack.append(s[i])
            elif s[i] ==")":
                stack.pop() # s is the valid paranthesis str
            if not stack :
                right = i 
                res.add(left)
                res.add(right)
                left = right + 1
                
        ans = ""
        for i in range(len(s)):
            if i not in res :
                ans += s[i]
        return(ans)
    
        
            