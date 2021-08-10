x=int(input("enter no. : "))
n=x
l=len(str(x))
s=0
while(l>0):
    digit=n%10
    s=s+digit*10**(l-1)
    n=n//10
    l=l-1
if x==s:
    print("pallindrome")
else:
    print("not a pallindrome")
