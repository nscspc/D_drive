y=0
l=[int(input("")),input(""),int(input(""))]
#while(y<3):
    #l[y]=input("")
    #print(' ',end="")
    #y=y+1
no=float(input("enter equation : "))
op=input('')
no2=float(input(""))
x=0
while(x<1):
    if(op=='+'):
        no=no+no2
        print(no)
        op=input('')
        no2=float(input(""))
    elif(op=='-'):
        no=no-no2
        print(no)
        op=input('')
        no2=float(input(""))
    elif(op=='*'):
        no=no*no2
        print(no)
        op=input('')
        no2=float(input(""))
    elif(op=='/'):
        no=no/no2
        print(no)
        op=input('')
        no2=float(input(""))
    else:
        print("wrong input")
        x=1

#print(no,op,no2)
