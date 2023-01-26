class Stack:
  
    def __init__(self, max=40):
        self.maxsize=max
        self.list=[]
        
    def push(self,new):
        if len(self.list)>=self.maxsize:
            print("stack overflow")
        else:
            return self.list.append(new)
          
    def pop(self):
        if len(self.list)==0:
            print("stack underflow")
        else:
            return self.list.pop()
          
    def traversal(self):
        for i in self.list:
            print(i, end=" ")
            
    def reverse(self):
        l2=self.list[::-1]
        for i in l2:
            print(i, end=" ")
            
    def top(self):
        return self.list[-1]
      
    def clear(self):
        return self.list.clear()
      
    def size(self):
        return len(self.list)
      
    def empty(self):
            return len(self.list)==0

