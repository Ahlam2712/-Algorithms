def evaluate_postfix(ex):
    stack=[]
    for i in ex:
        if i.isdigit():
            stack.append(i)
        else:
            x=stack.pop()
            y=stack.pop()
            stack.append(str(eval(y + i + x )))
    return float(stack.pop())
expr=input("enter your postfix expression: ")
print("result is ", evaluate_postfix(expr))
