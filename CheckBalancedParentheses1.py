open=['(','{','[']
close=[')','}',']']
def check(exp):
    stack=[]
    for i in exp:
        if i in open:
            stack.append(i)
        elif i in close:
            pos=close.index(i)
            if (len(stack)>0) and open[pos]==stack[-1]:
                stack.pop()
            else:
                return f'Unbalanced'
    if len(stack)==0:
        return 'Balanced'
    else:
        return 'UnBalanced'
