class Solution(object):
    def maxBottlesDrunk(self, n, ex):
        """
        Key Obeservasions:
        as long as we have full bottles(full>0)
            full = x 
            ex = e 
            empty = 0
            drunk += full
            empty += full ; full = 0
            full = 1 if ex <= emtpy else 0
            empty -= ex
            ex += 1   
        """
        full = n
        empty = 0
        res = 0
        count = 0
        while full>0:
            print full ,empty, ex
            res += full
            empty += full
            full = 0
            full = 1 if empty >= ex else 0
            empty -= ex 
            ex += 1
        print res
        return res
            
            