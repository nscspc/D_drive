#program of NUMBER SYSTEM CONVERSION

b=int(input("enter no of digits you want to enter in hexadecimal : "))
x=int(input("enter value : "))#hexadecimal value
l=len(str(x))
a=0
s=0
no=x
while(a<l):
    digit=no%10
    no=no//10
    s=s+digit*16**a
    a+=1

print(s)
