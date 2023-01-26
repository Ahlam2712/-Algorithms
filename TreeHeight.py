def height(root):
    
    if root is None:    
        return 0
        
    leftAns = height(root.left)
    rightAns = height(root.right)
    return max(leftAns, rightAns) + 1
