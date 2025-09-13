class MinStack(object):

    def __init__(self):
        self.nums = []
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        minValue = self.getMin()
        if minValue == None or minValue > val:
            minValue = val
        self.nums.append([val,minValue])
        

    def pop(self):
        """
        :rtype: None
        """
        self.nums.pop() if self.nums else None

        
        

    def top(self):
        """
        :rtype: int
        """
        return self.nums[-1][0] if self.nums else None
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.nums[-1][1] if self.nums else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()