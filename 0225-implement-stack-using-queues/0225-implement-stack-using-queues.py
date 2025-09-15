from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque() # main
        # self.q2 = deque() # auxillary

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)
        for _ in range(len(self.q1) - 1) : # alyas keep revers
            e = self.q1.popleft()
            self.q1.append(e)
        
        

    def pop(self):
        """
        :rtype: int
        """
         
        if len(self.q1) == 0 : return None
        return self.q1.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.q1) == 0 : return None
        return self.q1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()