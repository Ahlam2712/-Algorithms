def PostfixToPrefix(exp):
    stack = []
    operators = ['+', '-', '*', '/', '^']
    for i in exp:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = i + b + a
            stack.append(temp)
        else:
            stack.append(i)
    return stack
