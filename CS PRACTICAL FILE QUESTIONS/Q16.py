x=list()
y=list()
c=0
a=int(input("How many Values do you want to enter in FIRST Tuple : "))
while(c<a):
    x.append(input("Enter the Values in Tuple : "))
    c=c+1
b=int(input("How many Values do you want to enter in SECOND Tuple : "))
c=0
while(c<b):
    y.append(input("Enter the Values in Tuple : "))
    c=c+1
    
z=x+y
print("Tuple 1 : ",tuple(x))
print("Tuple 2 : ",tuple(y))

print(tuple(z))
