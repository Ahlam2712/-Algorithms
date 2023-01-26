#example 5+(5x20-5)/2-100*30
class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


def evaluateExpression(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return int(root.data)
    left_sum = evaluateExpression(root.left)
    right_sum = evaluateExpression(root.right)
    if root.data == '+':
        return left_sum + right_sum

    elif root.data == '-':
        return left_sum - right_sum

    elif root.data == '*':
        return left_sum * right_sum

    else:
        return left_sum / right_sum
#                 -
#        +                   x
#    5       /          100      30
#        -      2
#    x     5
# 5    20
root = node("-")
root.left = node("+")
root.left.left = node(5)
root.left.right = node("/")
root.left.right.right = node("2")

root.left.right.left = node("-")
root.left.right.left.right = node(5)

root.left.right.left.left = node("*")
root.left.right.left.left.left = node(5)
root.left.right.left.left.right = node(20)

root.right = node("*")
root.right.left = node(100)
root.right.right = node(30)
print(evaluateExpression(root))
