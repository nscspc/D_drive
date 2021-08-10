l=[4,5,21,7,8,98]
for x in range(len(l)):
    for i in range(x,len(l)):
        if l[i]>l[x]:
            tmp=l[x]
            l[x]=l[i]
            l[i]=tmp
print("second largest element of the given list : ",l[1])
