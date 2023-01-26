def Leaf_Count(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return Leaf_Count(root.left) + Leaf_Count(root.right)
