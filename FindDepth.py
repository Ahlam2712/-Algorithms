
def findDepth(root, x):
 
    if (root == None):
        return -1
    d = -1
    if (root.data == x):
        return d + 1

    d = findDepth(root.left, x)
    if d >= 0:
        return d + 1
    d = findDepth(root.right, x)
    if d >= 0:
        return d + 1
    return d
