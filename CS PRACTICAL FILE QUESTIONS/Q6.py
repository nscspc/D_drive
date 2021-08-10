y=0
x=0
while(x<3):
    marks=float(input("Enter MARKS:"))
    y=marks+y
    x+=1
avg=y/3
if avg>=90:
    print("A")
elif avg>=70:
    print("B")
elif avg>=60:
    print("C")
elif avg>=50:
    print("D")
else:
    print("FAIL")
