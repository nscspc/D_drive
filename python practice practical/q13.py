x=int(input("enter no. : "))
l=len(str(x))
y=0
s=0
n=x
while(y<l):
    digit=n%10
    s=s+digit**l
    n=n//10
    y=y+1
print(s)
if s==x:
    print(x,"is an ARMSTRONG NO.")
else:
    print(x,"is not an ARMSTRONG NO.")
