x=1
s=0
while(x<=7):
    b=str(x)
    t=float(input("enter temp of day "+b+" : "))
    s=s+t
    x=x+1
print(s/7)
