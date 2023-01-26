class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def depth(root):
    dep = 0
    while root is not None:
        dep += 1
        root = root.left
    return dep


def is_perfect(root, depth, level=0):
    if root is None:
        return True

    if root.left is None and root.right is None:
        return depth == level + 1
    if root.left is None or root.right is None:
        return False
    return is_perfect(root.left, depth, level + 1) and is_perfect(root.right, depth, level + 1)


#      6
#   4      8
# 3   5   7   9

root = node(6)
root.left = node(4)
root.left.left = node(3)
root.left.right = node(5)
root.right = node(8)
root.right.left = node(7)
root.right.right = node(9)


if is_perfect(root, depth(root)):
    print("It's a perfect Tree.")
else:
    print("It's not perfect.")

#if it is not
#      6
#   4      8
# 3   5   7

root2 = node(6)
root2.left = node(4)
root2.left.left = node(3)
root2.left.right = node(5)
root2.right = node(8)
root2.right.left = node(7)



if is_perfect(root2, depth(root2)):
    print("It's a perfect Tree.")
else:
    print("It's not perfect.")
