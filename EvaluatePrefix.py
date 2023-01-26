def evaluate_prefix(exp):
    ex=exp[::-1]
    stack=[]
    for i in ex:
        if i.isdigit():
            stack.append(i)
        else:
            x=stack.pop()
            y=stack.pop()
            stack.append(str(eval(x + i + y )))
    return float(stack.pop())
expr=input("enter your Prefix expression: ")
print("result is ", evaluate_prefix(expr))
