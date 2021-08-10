s=[]
c="y"
while(c=="y"):
    print("PUSH : 1")
    print("POP : 2")
    print("DISPLAY : 3")

    choice=int(input("Enter your choice : "))

    if choice==1:
        a=input("Enter the value you want to add in list : ")
        s.append(a)

    elif choice==2:
        if s==[]:
            print("Empty stack { list } ")
        else:
            b=print("Deleted element is :",s.pop())

    elif choice==3:
        if s!=[]:
            l=len(s)
            for i in range(l-1,-1,-1):
                print(s[i])
        else:
            print("Empty Stack { list }")
    else:
        print("wrong input")

    c=input("Do you want to continue ? y/n : ")
