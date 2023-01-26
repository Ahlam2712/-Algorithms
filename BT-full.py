class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def isFullTree(root):

    if root is None:
        return True

    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))

    return False
root = node(1)
root.right = node(3)
root.left = node(2)
root.left.left = node(4)
root.left.right = node(5)
root.left.right.left = node(6)
root.left.right.right = node(7)
if isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
