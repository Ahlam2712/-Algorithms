class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def search(root,key):

    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right,key)
    return search(root.left,key)
#      6
#   4      8
# 3   5   7   
root = node(6)
root.left = node(4)
root.left.left = node(3)
root.left.right = node(5)
root.right = node(8)
root.right.left = node(7)

if search(root,6) is None:
    print("element was not found")
else:
    print(f"{search(root,6).data} was found")
