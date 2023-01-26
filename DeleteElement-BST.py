
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
        return root
    if root.left is None and root.right is None:
        return None
    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    succParent = root
    succ = root.right
    while succ.left != None:
        succParent = succ
        succ = succ.left
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
    root.key = succ.key
    return root
