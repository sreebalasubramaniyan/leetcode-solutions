class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) ; n = len(matrix[0])
        
        col = [0] * n ; row= [0] * m 
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    col[j] = 1 
                    row[i] = 1 
        for i in range(m) :
            for j in range(n) :
                if col[j] == 1 or row[i] == 1 :
                    matrix[i][j] = 0 
        return 
        
        # Brut - 1
            # Time : O(m*n)
            # Space: O(1)

        def setRow(row) :
            for i in range(n) :
                if matrix[row][i] != 0 :
                    matrix[row][i] = 'x'
        def setCol(col) :
            for i in range(m) :
                if matrix[i][col] != 0 :
                    matrix[i][col] = 'x'
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    setRow(i)
                    setCol(j)
        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0 
        return 






        return 

        # At worst Case 
            # Time : 3*m*n ; O(m*n)
            # Space: m + n ; O(m+n)
        
        def rowZero(row) :
            for i in range(n) :
                matrix[row][i] = 0
        def colZero(col) :
            for i in range(m) :
                matrix[i][col] = 0

        row = set()
        column = set()
        for i in range(m) :
            for j in range(n):
                if matrix[i][j] == 0 :
                    row.add(i)
                    column.add(j)
        for i in row :
            rowZero(i)
        for j in column :
            colZero(j)



        