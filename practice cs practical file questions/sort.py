a=[5,4,6,2,4]
for i in range(5):
    for k in range(i,5):
        if a[i]>a[k]:
            tmp=a[i]
            a[i]=a[k]
            a[k]=tmp
print(a)
