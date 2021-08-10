x=int(input("Enter Integer"))
a=1
b=1
c=2
print(a,",",b,",",c,",",end=" ")
if x>=3:
    for i in range(x-3):
        d=c*b+a
        print(d,",",end=" ")
        a=b
        b=c
        c=d
