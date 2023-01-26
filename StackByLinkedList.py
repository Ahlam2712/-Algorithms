class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Stack:
    def __init__(self):
        self.head = None
        
    def push(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node

    def size(self):
        temp = self.head
        x = 0
        while temp.next:
            temp = temp.next
            x += 1
        if x == 0:
            return "empty"
        else:
            return x

    def is_empty(self):
        return True if self.head is None else False

    def pop(self):
        if self.is_empty():
            return "its Empty(Stack underflow)"
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
