class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class SLL:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        if temp is None:
            print("Empty")
        while temp:
            print(temp.data)
            temp=temp.next
        pass
      
    def addbeg(self,ndata):  
        nd = node(ndata)
        nd.next = self.head
        self.head = nd
       
        if self.head is None:
            nd = node(ndata)
            self.head = nd

        else:
            nd = node(ndata)
            nd.next = self.head
            self.head = nd
    
    def addend(self, ndata):
        ne = node(ndata)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
    
    
    def addp(self, ndata, pos):
        pos = pos - 1
        np = node(ndata)
        temp = self.head
        for i in range(pos):
            temp = temp.next
        np.next = temp.next
        temp.next = np
        
     def delb(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def dele(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def delp(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
   
       
