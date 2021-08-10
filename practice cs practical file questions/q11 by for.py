no=int(input("enter limit : "))
print("0, 1",end="")
a=0
b=1
for i in range(no-2):
    c=b+a
    print(",",c,end="")
    a=b
    b=c
