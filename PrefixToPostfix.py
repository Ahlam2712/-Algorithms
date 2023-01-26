def PrefixToPostfix(exp)
    stack = []
    operators = ['+', '-', '*', '/', '^']
    ex = exp[::-1]
    for i in ex:
        if i in operators:
            a = stack.pop()
            b = stack.pop()
            temp = a + b + i
            stack.append(temp)
        else:
            stack.append(i)
    return stack
