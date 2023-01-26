from collections import deque
class Queue:
    def __init__(self, max=50):
        self.queue=deque()
        self.max = max

    def enqueue(self, nd):
        if len(self.queue) == self.max:
            print("queue is full")
        else:
            return self.queue.append(nd)

    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is Empty")
        else:
            return self.queue.popleft()
    def isEmpty(self):
        return len(self.queue) == 0
    def getsize(self):
        return len(self.queue)
