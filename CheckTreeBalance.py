class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def height(root):

    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return max(left, right) + 1


def is_Balanced(root):
    if root is None:
        return True

    left_h = height(root.left)
    right_h = height(root.right)


    if abs(left_h - right_h) <= 1 and is_Balanced(root.left) is True and is_Balanced(root.right) is True:
        return True

    return False
# First Try when it is.
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


if is_Balanced(root):
    print("Tree Is Balanced. ")
else:
    print("Tree Is Not Balanced. ")

#second try when it is not
#         6
#      4      8
#    3   5
#  2

root2 = node(6)
root2.left = node(4)
root2.left.left = node(3)
root2.left.left.left=node(2)
root2.left.right = node(5)
root2.right = node(8)

if is_Balanced(root2):
    print("Tree Is Balanced. ")
else:
    print("Tree Is Not Balanced. ")
