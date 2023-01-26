def maxValue(root):

    if (root == None):
        return float('-inf')
    now = root.data
    lnow = maxValue(root.left)
    rnow = maxValue(root.right)
    if (lnow > now):
        now = lnow
    if (rnow > now):
        now = rnow
    return now
