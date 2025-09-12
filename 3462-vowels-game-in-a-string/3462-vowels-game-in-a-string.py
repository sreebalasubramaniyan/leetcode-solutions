class Solution(object):
    def doesAliceWin(self, s):
        """
        
        """
        v = 0
        for i in s:
            if i.lower() in "aeiou": v+=1
        if not v : return False
        return True
        # 0 1 2 2 2 3 3 4 4     -4
        # alice wanto choose the substr that the remaining substring
        # should have the odd voewels
        # other wise bob will delete the whole string and wins
        # (for for same as bob)

        # 0..1..2...3....4

        eeoe
