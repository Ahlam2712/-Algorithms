class node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,ndata):
        if self.head is None:
            ne = node(ndata)
            self.head=ne
            self.tail=self.head
        else:
            ne=node(ndata)
            temp=self.tail
            temp.next=ne
            self.tail=ne

    def dequeue(self):
        if self.head==None:
            print("empty")
        temp=self.head
        self.head=temp.next
        temp.next=None

    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data, end=" ")
            temp = temp.next
