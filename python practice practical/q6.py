a=int(input("enter marks of 1st subject : "))
b=int(input("enter marks of 2nd subject : "))
c=int(input("enter marks of 3rd subject : "))
av=a+b+c
avg=av/3
print(avg)
if avg>90:
    print("a")
elif avg>70:
    print("b")
elif avg>50:
    print("c")
else:
    print("fail")
