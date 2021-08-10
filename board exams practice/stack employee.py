s=[]
c="y"
while(c=="y"):
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. DISPLAY WHOLE LIST")
    
    choice=input("enter choice : ")

    if choice=="1":
        a=input("enter employee id : ")
        b=input("enter employee name : ")
        x=[a,b]
        s.append(x)

    elif choice=="2":
        if s==[]:
            print("stack empty")
        else:
            print("deleted element is :",s.pop())

    elif choice=="3":
        for i in range(len(s)-1,-1,-1):
            print(s[i])

    elif choice=="4":
        print(s)
        
    else:
        print("wrong input")

    c=input("do you want to continue (y/n) : ")
