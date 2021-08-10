x=int(input("enter limit : "))
c=0
z=3
fact=0
if x!=0:
    print('2')
    c=c+1
while(c<x):
    m=2
    while(m<=z/2):
        if z%m==0:
            fact=1
        m=m+1
    if fact==1:
        print(end="")
    else:
        print(z)
        c=c+1
    z=z+1
    fact=0
