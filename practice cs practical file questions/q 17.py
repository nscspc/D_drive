lst=[12,1,2,3,4,5,6,7,8,9,80,50,7,90,50,40,12,15,]
y=[]
for i in lst:
    if i%2==0:
        y.append(i)
print(lst)
print(y)
x=[]
a=0
l=len(y)
b=l
while(l>0):
    if a!=b-1:
        if y[a]>y[a+1]:
            if x!=[]:
                c=0
                l2=len(x)
                if c<=len(x)-1:
                    
                    while(l2>0):
                        if x[c]<y[a]:
                            x.insert(c,y[a])
                            flag=1
                        l2=l2-1
                        c=c+1
                        if flag==1:
                            l1=0
                    if flag==0:
                        x.append(y[a+1])
                        
                else:
                    if y[a-1]>y[a+1]:
                        x.append(y[a-1])
                    else:
                        x.append(y[a+1])
            if x==[]:
                x.append(y[a])
        else:
            if x!=[]:
                d=0
                l1=len(x)
                flag=0
                while(l1>0):
                    if y[a+1]>x[d]:
                        x.insert(d,y[a+1])
                        flag=1
                    l1=l1-1
                    d=d+1
                    if flag==1:
                        l1=0
                if flag==0:
                    x.append(y[a+1])
                    
    else:
        flag=0
        for i in y:
            z=x.count(i)
            if z==0:
                x.append(i)       
    l=l-1
    a=a+1
    print(x)
if b!=0:
    print(x[0])
else:
    print("no even number")
print(x)
