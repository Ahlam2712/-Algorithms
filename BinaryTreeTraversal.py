#DFS
class BT:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end=" ")
def Preorder(root) :
    if root :
        print(root.data,end=" ")
        Preorder(root.left)
        Preorder(root.right)
#BFS

from queue import Queue
def BFS(root):
    q=Queue()
    q.put(root)
    while not q.empty():
        curr=q.get()
        print(curr.data)
        if curr.left!=None:
            q.put(curr.left)
        if curr.right!=None:
            q.put(curr.right)


