class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def sum_tree(root):
    sum = 0
    q = []
    q.append(root)
    while len(q) > 0:
        temp = q.pop(0)
        sum += temp.data
        if (temp.left != None):
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)
    return sum
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
print(sum_tree(root))
