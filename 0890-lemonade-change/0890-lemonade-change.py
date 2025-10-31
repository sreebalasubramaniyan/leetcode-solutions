class Solution(object):
    def lemonadeChange(self, bills):
        """
        pays
         0 : five += 1
         5 : we need atleas one five 
         15 : we need atleaset one ten and one five or threefive

        """
        five = ten = twen = 0 
        for i in bills:
            change = abs(i-5)
            if change == 0:
                five += 1
            elif change == 5:
                if not five:
                    return False
                five -= 1 ; ten += 1
            elif change == 15:
                if ten and five :
                    twen += 1
                    ten -= 1 ; five -=1
                    continue
                elif five >= 3:
                    five -= 3
                    twen += 1
                    continue
                return False
        return True 