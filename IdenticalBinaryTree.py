class node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def ident(t1, t2):
    if t1 is None and t2 is None:
        return True
    return t1 is not None and t2 is not None and (t1.data == t1.data) and ident(t1.left, t1.left) and ident(t1.right, t2.right)
