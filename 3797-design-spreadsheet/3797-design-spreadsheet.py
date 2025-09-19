class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.mat = [[0 for _ in range(26)] for i in range(rows)]

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        row = int(cell[1:]) - 1
        col = alpha.index(cell[0])

        self.mat[row][col] = value

       

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        row = int(cell[1:]) - 1
        col = alpha.index(cell[0])

        self.mat[row][col] = 0

        

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = 0
        x,y = formula[1:].split("+")
        if x[0].isalpha() :
            row = int(x[1:]) - 1
            col = alpha.index(x[0])
            res += self.mat[row][col]
        elif x.isdigit() : res += int(x)
        if y[0].isalpha() :
            row = int(y[1:]) - 1
            col = alpha.index(y[0])
            res += self.mat[row][col]
        elif y.isdigit() : res += int(y)
        return res



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)