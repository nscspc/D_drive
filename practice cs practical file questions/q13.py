x=int(input("enter no. : "))
l=len(str(x))
a=1
s=0
y=x
while(a<=l):
    digit=y%10
    s=s+digit**l
    y=y//10
    a=a+1
if s==x:
    print(x,"is an armstrong no.")
else:
    print(x,"is not an armstrong no.")
