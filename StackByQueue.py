from queue import LifoQueue
class Stack:
    def __init__(self,max=50):
        self.max = max
        self.stack=LifoQueue(maxsize=self.max)
      
    def push(self,nd):
            return self.stack.put(nd)

    def pop(self):
            return self.stack.get()

    def isempty(self):
        return self.stack.empty()

    def size(self):
        return self.stack.qsize()
