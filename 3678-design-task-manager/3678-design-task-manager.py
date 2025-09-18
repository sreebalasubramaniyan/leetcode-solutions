class TaskManager(object):
    def __init__(self, tasks):
        self.rank = SortedList()
        self.Store = {}
        for u,t,p in tasks:
            self.rank.add((p,t))
            self.Store[t] = (p,u)
    def add(self, u, t, p):
        self.Store[t] = (p,u)
        self.rank.add((p,t))
    def edit(self, t, new):
        old,user = self.Store[t]
        self.rank.remove((old,t))
        del self.Store[t]
        self.add(user,t,new)
    def rmv(self, t):
       
        p,user = self.Store[t]
        del self.Store[t]
        self.rank.remove((p,t))
        

    def execTop(self):
        if not self.rank : 
            return -1
        else:
            p,t = self.rank[-1]
            res = self.Store[t][1]
        self.rank.pop()
        return res

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()