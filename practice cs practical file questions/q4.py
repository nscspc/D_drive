n1=int(input("enter no. 1 : "))
n2=int(input("enter no. 1 : "))
n3=int(input("enter no. 1 : "))

if n1>n2 and n1>n3:
    print("n1 is greater")
elif n1<n2 and n2>n3:
    print("n2 is greater")
elif n3>n2 and n1<n3:
    print("n3 is greater")
else:
    print("all are equal")
