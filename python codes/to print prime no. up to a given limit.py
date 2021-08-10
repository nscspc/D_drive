x=int(input("Enter the limit of PRIME Numbers :"))
y=2
m=2
flag=0
while(x>1):
    m=2
    flag=0
    while(m<=y/2):
        if (y%m==0):
            flag=1
        m=m+1
    if flag==0:
        print(y,end=" ")
    y=y+1
    x=x-1
