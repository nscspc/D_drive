x=1
a=1
z=1
while(x<=4):
    y=3
    while(y>=x):
        print(" ",end="")
        y=y-1
    while(z>=1):
        print(" *",end="")
        z=z-1
    a=a+1
    print()
    z=z+a
    x=x+1
