class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        row = 0
        col =  


        """
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >=0 : 
            a = matrix[r][c] 
            if a == target : 
                return True
            elif a > target :
                c -= 1 
            else:
                r += 1
        return False