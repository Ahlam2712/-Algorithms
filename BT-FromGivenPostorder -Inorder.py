class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
def buildUtil(In, post, inst ,inend, pindex):
    if (inst > inend):
        return None
    node = Node(post[pindex[0]])
    pindex[0] -= 1
    if (inst == inend):
        return node
    iIndex = search(In, inst, inend, node.data)
    node.right = buildUtil(In, post, iIndex + 1,
                           inend, pindex)
    node.left = buildUtil(In, post, inst,iIndex - 1, pindex)
    return node
def buildTree(In, post, n):
    pindex = [n - 1]
    return buildUtil(In, post, 0, n - 1, pindex)
def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value):
            break
    return i
def preorder(node):
    if node == None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

In = [36, 11, 27, 42, 30, 9, 77, 12]
post = [11, 36, 42, 27, 9, 12, 77, 30]
n = len(In)
root = buildTree(In, post, n)
print("Preorder of the tree: ")
preorder(root)
