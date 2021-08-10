n=int(input("enter integer : "))
l=len(str(n))
sum=0
for i in range(l):
    digit=n%10
    sum+=digit
    n//=10
print("sum of digits of inputted no. is :",sum)
