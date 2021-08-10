l=[1,2,3,4,5]
l1=len(l)
a=0
for i in l:
    c=0
    for x in range(0,l1):
        if i==l[x]:
            c=c+1
    print("frequency of",i,"is : ",c)
