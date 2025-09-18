class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.rank = SortedList()
        self.Store = {}
        for u,t,p in tasks:
            self.rank.add((p,t))
            self.Store[t] = (p,u)
        print self.Store
        print self.rank
        

    def add(self, u, t, p):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.Store[t] = (p,u)
        self.rank.add((p,t))
        print self.Store
        print self.rank

    def edit(self, t, new):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        old,user = self.Store[t]
        self.rank.remove((old,t))
        del self.Store[t]
        self.add(user,t,new)
        print self.Store
        print self.rank

    def rmv(self, t):
        """
        :type taskId: int
        :rtype: None
        """
        p,user = self.Store[t]
        del self.Store[t]
        self.rank.remove((p,t))
        print self.Store
        print self.rank
        

    def execTop(self):
        """
        :rtype: int
        """
        print self.Store
        print self.rank
        
        if not self.rank : 
            return -1
        else:
            p,t = self.rank[-1]
            res = self.Store[t][1]
        self.rmv(t)
        return res

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()