x=int(input("Enter the limit of FIBONACCI SERIES :"))
y=1
a,b=0,1
if x!=0:
    print(a,",",b,end=" ")
    while(y<=x):
        print(",",b,end=" ")
        a=b
        b=b+a
        y=y+1
else:
    print()
