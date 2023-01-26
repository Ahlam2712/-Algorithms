class Stack:
    def __init__(self):
        self.list=[]
    def push(self,new):
        return self.list.append(new)
    def pop(self):
        return self.list.pop()
    def top(self):
        return self.list[-1]
    def clear(self):
        return self.list.clear()
    def size(self):
        return len(self.list)
    def empty(self):
        if len(self.list)==0:
            return True #its empty
        else:
            return False #No its not empty
    def display(self):
        for i in self.list:
            print(i,end=" ")

output=Stack()
redo=Stack()
def write(newdata):
    output.push(newdata)
    return output
def redof():
    x=output.pop()
    redo.push(x)
    return output
def undof():
    h=redo.pop()
    output.push(h)
    return output
def read():
    output.display()

def main():

    m="w"
    while m=="w" :
        print("what you want to do: ")
        print("1) Write \n2) redo \n3) undo \n4)Read \n5)finish")
        wh = int(input("Enter Your option:(Numbers please) "))

        if wh==1:
            nd=input("Enter what you want to write: ")
            write(nd)
        elif wh==2:
            redof()
        elif wh==3:
            undof()
        elif wh==4:
            read()
        elif wh==5:
            m="r"
        else:
            wh=int(input("Out of the available options try again: "))
    else:
        read()
main()
