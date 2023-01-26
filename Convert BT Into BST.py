class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def storeInorder(root, inorder):
    if root is None:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)

def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1

def arrayToBST(arr, root):
    if root is None:
        return
    arrayToBST(arr, root.left)
    root.data = arr[0]
    arr.pop(0)
    arrayToBST(arr, root.right)

def binaryTreeToBST(root):
    if root is None:
        return
    n = countNodes(root)
    arr = []
    storeInorder(root, arr)
    arr.sort()
    arrayToBST(arr, root)

root = node(5)
root.left = node(32)
root.right = node(22)
root.left.left = node(27)


binaryTreeToBST(root)

