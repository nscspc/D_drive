#program to perform BINARY SEARCH
def binarysearch(a,low,high,value):
    if high<low:
        return None
    midval=(low+high)//2
    
    if a[midval]>value:
        return binarysearch(a,low,high-1,value)
    elif a[midval]<value:
        return binarysearch(a,low+1,high,value)
    else:
        return midval

l=[]
n=int(input("enter no. of elements that you want to enter in list : "))
for i in range(0,n):
    l.insert(i,int(input("enter : ")))
x=int(input("enter low index : "))
y=int(input("enter high index : "))
z=int(input("enter value that you want to search : "))
c=l.count(z)
for i in range(0,n):
    for j in range(0,n):
        if(l[i]<l[j]):
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)
while(c>0):
    p=binarysearch(l,x,y,z)
    print(p)
    l.insert(p,z-1)
    c-=1

'''def binarysearch(a,low,high,value):
    if high<low:
        return None
    midval=(low+high)//2
    if list[midval]>value:
        return binarysearch(a,low,high-1,value)
    elif list[midval]<value:
        return binarysearch(a,low+1,high,value)
    else:
        return midval'''
