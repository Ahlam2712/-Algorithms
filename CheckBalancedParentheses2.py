def is_match(c1,c2):
    match_dict={
        ')':'(',
        ']':'[',
        '}':'{'
    }
    return match_dict[c1] == c2 #True or False

def is_balanced(s):
    s1=[]
    for i in s:
        if i=='(' or i=='[' or i=='{':
            s1.append(i)
        if i == ')' or i == ']' or i == '}':
            if len(s1)==0:
                return False
            if not is_match(i, s1.pop()):
                return False
    return len(s1) == 0
