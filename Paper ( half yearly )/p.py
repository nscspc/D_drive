x=input("enter no. : ")
str1=" "
a=0
while(a<len(x)):
    str1=x[a]+str1
    a=a+1
if str1==x:
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
