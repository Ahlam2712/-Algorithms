s1output=[]
s2operator=[]
priority={"(":0,"+":1, "-":1,"*":2,"/":2,"^":3}
exp = input("Enter the infix Expression: ")
for ch in exp:
    if ch=="(":
        s2operator.append(ch)
    elif(ch==")"):
        while s2operator[-1]!="(":
            ele=s2operator.pop()
            s1output.append(ele)
        s2operator.pop()
    elif (ch=="+" or ch=="-" or ch=="/" or ch=="*" or ch=="^"):
        if(len(s2operator)>0):
            while priority[s2operator[-1]]>=priority[ch]:
                ele=s2operator.pop()
                s1output.append(ele)
                if(s2operator)==0:
                    break
        s2operator.append(ch)
    else:
        s1output.append(ch)
while(len(s2operator)!=0):
    ele=s2operator.pop()
    s1output.append(ele)
print(s1output)
