class Solution(object):
    def removeSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        st = [] ; close = open = 0
        for idx,val in enumerate(s):
            if val == '(':
                open += 1
                st.append(('(',open))
            else:
                close += 1
                st.append((')',close))
            
           
            if val == ')' and len(st) >= 2*k :
                # Check valid valid len
                nst = len(st)
                if  st[nst-k][0] == ')' and st[nst-2*k][0] == '(' and st[nst-k-1][0]=='(' :
                        a = st[-1][1] - st[nst-k][1] + 1
                        b = st[nst-k-1][1] - st[nst-2*k][1] + 1
                        
                        if a==b==k:
                            for i in range(2*k):
                                st.pop()
                            open -= k if open > k else 0 
                            close -= k if close > k else 0

        res = ""
        for c,idx in st:res+=c
        return res