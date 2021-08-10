x=list()
c=0
a=int(input("How many Values do you want to enter in the LIST of Integers : "))
while(c<a):
    x.append(int(input("Enter the Values in List : ")))
    c=c+1

i=0
c=0
y=list()
while(c<a):
    if x[i]%2==0:
        y.append(x[i])
    else:
        print(end="")
    c=c+1
    i=i+1
        
if len(y)!=0:
    print("The Largest EVEN no. in the List of Integers is :",max(y))
else:
    print("No EVEN no.")
