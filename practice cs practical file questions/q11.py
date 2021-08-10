x=int(input("enter limit:"))
a,b=0,1
print(a,",",b,end=" ")
for i in range(x-2):
    c=a+b
    a,b=b,c
    print(",",c,end=" ")
