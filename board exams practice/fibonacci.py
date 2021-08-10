x=int(input("enter limit : "))
y,a,b=2,0,1
print(a,",",b,end=" ")
while(y<x):
    c=a+b
    print(",",c,end=" ")
    a,b,y=b,c,y+1
    
