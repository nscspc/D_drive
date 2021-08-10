x=int(input("enter limit : "))
y=2
a,b=0,1
print(a,",",b,end=" ")
while(y<x):
    c=a+b
    print(",",c,end=" ")
    a=b
    b=c
    y=y+1
    
