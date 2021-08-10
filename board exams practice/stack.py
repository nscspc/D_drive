s=[]
c="y"
while(c=="y"):
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")

    choice=input("enter choice : ")

    if choice=="1":
        a=input("enter the value you want to enter : ")
        s.append(a)

    elif choice=="2":
        if s==[]:
            print("stack empty")
        else:
            print("deleted element is :",s.pop())

    elif choice=="3":
        for i in range(len(s)-1,-1,-1):
            print(s[i])

    else:
        print("wrong input")

    c=input("do you want to continue (y/n) : ")
