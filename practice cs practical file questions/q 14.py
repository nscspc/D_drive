x=int(input("enter no. : "))
s=0
l=len(str(x))-1
y=x
while(l>=0):
    digit=y%10
    s=s+digit*10**l
    y=y//10
    l=l-1
if x==s:
    print(x,"is pallindrome")
else:
    print(x,"is not palindrome")
