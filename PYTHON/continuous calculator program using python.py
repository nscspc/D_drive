global n1
x=0
var=True

def add():
    global n1
    if(x==0):
        n1=float(eq[0:i])
    n2=float(eq[i+1:l+1])
    n1+=n2
    print(n1,end="")

def sub():
    global n1
    if(x==0):
        n1=float(eq[0:i])
    n2=float(eq[i+1:l+1])
    n1-=n2
    print(n1,end="")

def mul():
    global n1
    if(x==0):
        n1=float(eq[0:i])
    n2=float(eq[i+1:l+1])
    n1*=n2
    print(n1,end="")

def div():
    global n1
    if(x==0):
        n1=float(eq[0:i])
    n2=float(eq[i+1:l+1])
    n1/=n2
    print(n1,end="")

while var:
    eq=input("")
    l=len(eq)

    for i in range(0,l):
        if(eq[i]=='+'):
            add()
            break
        
        elif(eq[i]=='-'):
            sub()
            break
        
        elif(eq[i]=='*'):
            mul()
            break
        
        elif(eq[i]=='/'):
            div()
            break
        
        else:
            var2=True
            if(i==l-1):
                print("you have entererd invalid operator ")
                while var2:
                    choice=input("do you want to continue (Y/N) ? :")
                    if(choice=='y' or choice=='Y'):
                        var=True
                        var2=False
                        x=-1
                    elif(choice=='n' or choice=='N'):
                        var=False
                        var2=False
                        x=-1
                    else:
                        print("invalid input")
                        var2=True
    x+=1
