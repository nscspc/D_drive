x=int(input("Enter NO."))
y=1
a=list()
while(y<=x):
    a.append(int(input("enter no.")))
    y=y+1
print(a)
b=a.reverse()
if a==b:
    print("yes")
else:
    print("no")
