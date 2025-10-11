class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = self.prev = None
class LRUCache(object):
    def deladd(self,node):
        if node == self.end:
            if node.prev :
                t = self.end.prev
                self.end.prev.next = None
                self.end.prev = None
                self.end = t 
            else:
                self.head = self.end 
        elif node == self.head:
            return
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        node.next = self.head
        self.head.prev = node
        self.head = node
            
    def __init__(self, capacity):
       self.look = {}
       self.Len = capacity
       self.head = self.end = None
        

    def get(self, key):
        if key not in self.look:
            return -1
        node = self.look[key]
        res = node.val
        self.deladd(node)
        return res  
        

    def put(self, key, val):

        if len(self.look) >= self.Len and key not in self.look:
            k = self.end.key
            if self.end.prev:
                t = self.end.prev
                self.end.prev.next = None
                self.end.prev = None 
                self.end = t
            else:
                self.end = self.head = None
            del self.look[k]
        if self.head == None:
            self.head = Node(key,val)
            self.end  =  self.head
            self.look[key] = self.head
        else:
            if key not in self.look:
                newNode = Node(key,val)
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.look[key] = newNode
            else:
                node = self.look[key]
                self.deladd(node)
                self.head.val = val
           
                

        

