m=2
x=int(input("Enter the limit of PRIME Numbers :"))
while(m<=x):
    y,z=2,0
    while(y<=m/2):
        if m%y==0:
            z=1
        y=y+1
    if z==0:
        print(m)
    m=m+1
