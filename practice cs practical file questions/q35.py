q=[]
c="y"
while(c=="y"):
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")

    choice=input("Enter your choice : ")
    if choice=='1':
        x=int(input("Enter value : "))
        q.append(x)
    elif choice=='2':
        if  q==[]:
            print("Queue Empty")
        else:
            print("Deleted element is :",q.pop(0))
    elif choice=="3":
        for i in q:
            print(i)
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
