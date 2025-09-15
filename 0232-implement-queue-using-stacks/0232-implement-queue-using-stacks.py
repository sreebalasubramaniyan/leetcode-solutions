class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []
    def push(self,x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.st1) == 0 : return None
        while len(self.st1) > 1 :
            e = self.st1.pop()
            self.st2.append(e)
        poped = self.st1.pop()
        
        while len(self.st2) > 0:
            e = self.st2.pop()
            self.st1.append(e)
        return poped
        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.st1) == 0 : return None
        while len(self.st1) > 1 :
            e = self.st1.pop()
            self.st2.append(e)
        Top = self.st1[0]
        while len(self.st2):
            e = self.st2.pop()
            self.st1.append(e)
        return Top
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.st1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()