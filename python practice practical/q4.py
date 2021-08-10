a=int(input("enter value : "))
b=int(input("enter value : "))
c=int(input("enter value : "))
if a>b and a>c:
    print("a is greater")
elif a<b and b>c:
    print("b is greater")
elif c>b and a<c:
    print("c is greater")
else:
    print("all are equal")
