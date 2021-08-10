s=[]
c="y"
while(c=="y"):
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")

    choice=input("Enter your choice : ")
    if choice=="1":
        x=int(input("enter value : "))
        s.append(x)
    elif choice=="2":
        if s==[]:
            print("Empty Stack")
        else:
            print("deleted element is :",s.pop())
    elif choice=="3":
        l=len(s)
        for i in range(l-1,-1,-1):
            print(s[i])
    else:
        print("Wrong Input")
    var=True
    while(var==True):
        ch=input("Do you want to continue ? (y/n) : ")
        if ch=="Y" or ch=="y":
            c="y"
            var=False
        elif ch=="n" or ch=="N":
            c="n"
            var=False
        else:
            print("Wrong Input")
