#program of NUMBER SYSTEM CONVERSION

x=int(input("enter value : "))#octal value
l=len(str(x))
a=0
s=0
no=x
while(a<l):
    digit=no%10
    no=no//10
    s=s+digit*8**a
    a+=1

print(s)
