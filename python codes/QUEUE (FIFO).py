q=[]
c="y"
while(c=="y"):
    print("PUSH : 1")
    print("POP : 2")
    print("DISPLAY : 3")

    choice=int(input("Enter your choice : "))

    if choice==1:
        a=input("Enter the value that you want to add in list : ")
        q.append(a)

    elif choice==2:
        if q==[]:
            print("Empty Queue { list }")
        else:
            b=print("Deleted element is :",q.pop(0))

    elif choice==3:
        if q!=[]:
            l=len(q)
            for i in range(0,l):
                print(q[i])
        else:
            print("Empty Queue { list }")
    else:
        print("Wrong Input")

    c=input("do you want to continue ? y/n : ")
