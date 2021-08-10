l=[1,2,3,4,5,6,7,8,9,10]
no=int(input("enter value : "))
l1=len(l)
while(l1>=0):
    l1=l1-1
    if no==l[l1]:
        break
    
print(l1)
