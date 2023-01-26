def minValue(root):
    if root is None:
        return float('inf')
    now = root.data
    lnow = minValue(root.left)
    rnow = minValue(root.right)
    if lnow < now:
        now = lnow
    if rnow < now:
        now = rnow
    return now
