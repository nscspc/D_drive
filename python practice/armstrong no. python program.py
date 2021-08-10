x=int(input("enter no. : "))
c=x
i=0
s=0
while(i<=len(str(x))):
      d=c%10
      c=c//10
      s=s+d**len(str(x))
      i+=1
if(x==s):
      print(x,"is an ARMSTRONG number .")
else:
    print(x,"is not an ARMSTRONG number .")
