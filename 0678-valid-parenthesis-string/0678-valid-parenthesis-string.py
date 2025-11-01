class Solution(object):
    def checkValidString(self, s):
        """
        some observation

        two stack
        open = []
        stars = []

        push the inddieces

        *)
        ()
    other cases 
        )***(())
        star = 
        open = 
        return False
   1)    * ( ) * ( ) ( * ) * *
        0 1 2 3 4 5 6 7 8 9 10

        open = 
        star = 0 3 7  9 10
        
        at the end ? 
        
        if not open : reutrn True
    2)  ( * * ) )
        0 1 2 3 4
        open = 
        star = 1   


   3)   ( ( ( ) * * * ( 
        0 1 2 3 4 5 6 7

        open = 7 1 6 
        star = 4 5 6 


        we can do that greedy method
        after greddy True else : False


        """
        star = []
        open = []

        for idx,c in enumerate(s):
            if c == '(':
                open.append(idx)
            elif c == ')': # this is crutial part right ?
                if open :
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else: # c = *
                star.append(idx)
        if open:
            for i in open[::-1]:
                if star and star[-1] > i:
                    star.pop()
                else:
                    return False
            return True 
        else:
            return True
                        
    
        