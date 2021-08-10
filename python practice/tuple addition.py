t1=tuple()
t2=tuple()
n1=int(input("enter no. of elements you want to enter in first tuple : "))
for i in range(0,n1):
    t1.append(input("enter : "))
n2=int(input("enter no. of elements you want to enter in second tuple : "))
for i in range(0,n2):
    t1.append(input("enter : "))
t3=tuple()
t3=t1+t2
for i in range(0,n1+n2):
    print(t3[i],end=" ")
