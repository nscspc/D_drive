x=list()
c=0
a=int(input("How many Values do you want to enter in the LIST of Integers : "))
while(c<a):
    x.append(int(input("Enter the Values in List : ")))
    c=c+1
x.remove(max(x))
print("The Second Largest Element of the List is :",max(x))
