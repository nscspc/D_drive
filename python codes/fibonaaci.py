limit=int(input("enter the limit : "))
a,b=0,1
print(a,end=" ")
while(b<=limit):
    print(",",b,end=" ")
    a,b=b,a+b
