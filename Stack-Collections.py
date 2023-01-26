from collections import deque
class Stack:
    def __init__(self,max=50):
        self.stack=deque()
        self.max=max

    def push(self,nd):
        if len(self.stack)==self.max:
            print('stack overflow')
        else:
            return self.stack.append(nd)
    
    def pop(self):
        if len(self.stack)==0:
            print('stack underflow')
        else:
            return self.stack.pop()
        
    def isempty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
