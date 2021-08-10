heightincm=int(input("enter height in cm"))
x=heightincm/2.54
y=x/12
while(heightincm>0):
    print("height in inches =",x)
    heightincm=heightincm-heightincm
while(x>0):
    print("height in feet =",y)
    x=x-x

