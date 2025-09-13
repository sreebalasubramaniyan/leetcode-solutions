class MyStack(object):

    def __init__(self):
        self.st = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.st.pop() if self.st else None 
        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1] if self.st else None

    def empty(self):
        """
        :rtype: bool
        """
        return True if not self.st else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()