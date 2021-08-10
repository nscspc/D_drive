x=list()
c=0
a=int(input("How many Values do you want to enter in the LIST of Integers : "))
while(c<a):
    x.append(input("Enter the Values in List : "))
    c=c+1
k,i=0,0
#while(k<len(x)):
while(i<len(x)):
    b=0
    z=x[i]
    y=x.count(z)
    print("frequency of","'",z,"'","is",y)
    while(b<y):
        x.remove(z)
        b=b+1
    #k=k+1
