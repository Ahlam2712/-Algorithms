class Queue:
    def __init__(self,max=50):
        self.list=[]
        self.max=max
    def enqueue(self,nd):
        if len(self.list)==self.max:
            print("queue is full")
        else:
            return self.list.append(nd)
    def dequeue(self):
        if len(self.list) == 0:
            print("queue is Empty")
        else:
            return self.list.pop(0)
    def isEmpty(self):
        return len(self.list)==0
    def getsize(self):
        return len(self.list)
