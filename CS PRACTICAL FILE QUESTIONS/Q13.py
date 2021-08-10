num=int(input("Enter no. : "))
temp,s,order=num,0,len(str(num))
while temp>0:
    digit=temp%10
    s=s+digit**order
    temp//=10
if num==s:
    print(num,"is an Armstrong no.")
else:
    print(num,"is not an Armstrong no.")
