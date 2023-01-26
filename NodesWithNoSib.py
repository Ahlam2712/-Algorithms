
def printSingles(root):
    if root is None:
        return

    if root.left is not None and root.right is not None:
        printSingles(root.left)
        printSingles(root.right)

    elif root.right is not None:
        print(root.right.data, end=" ")
        printSingles(root.right)

    elif root.left is not None:
        print(root.left.data, end=" ")
        printSingles(root.left)


#      6
#   4      8
# 3   5   7   9
#2              19
root = node(6)
root.left = node(4)
root.left.left = node(3)
root.left.left.left = node(2)
root.left.right = node(5)
root.right = node(8)
root.right.left = node(7)
root.right.right = node(9)
root.right.right.right = node(19)
printSingles(root)
