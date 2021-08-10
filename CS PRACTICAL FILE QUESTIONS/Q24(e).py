x=1
z=1
while(x<=4):
    y=1
    while(y<=x):
        print(z,end=" ")
        y=y+1
        if y<=x:
            z=z+1
    else:
        print()
        x=x+1
        if z<=1:
            z=z+1
        elif z==5:
            z=z-1
