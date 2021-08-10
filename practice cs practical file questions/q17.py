lst=[5,7,4,12,0,45]
y=[]
for i in lst:
    if i%2==0:
        y.append(i)
print(y)
for x in range(len(y)):
    for i in range(x,len(y)):
        if y[x]<y[i]:
            tmp=y[x]
            y[x]=y[i]
            y[i]=tmp
print("LIST elements AFTER SORTING :",y)

if y!=[]:
    print(y[0])
else:
    print("no even number")

