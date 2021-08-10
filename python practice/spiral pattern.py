l=[]
g=1
#[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i=1
x=4
y=0
z=x-1
b=x
c=1
while(i<=x**2):
    if(g==1):
        while(y<=z):#0
            l.insert(y,i)
            i+=1
            y+=c#1234#11 15
        y-=c;#3 #15
    else:
        while(y>=z):#0
            l.insert(y,i)
            i+=1
            y+=c#1234#11 15
        y-=c;#3 #15
    if(y==x-1):
        c=b#
        y+=c#7
        z=x**2-1#15
        g=1
    elif(y==x**2-1):
        c=-1
        y=y+c
        z=x**2-x-1
        g=0
    elif(y==x**2-x-1):
        c=-b
        y+=c
        z=x+1
    elif(y==x+1):
        c=1
        y+=c
        z=2*x-2
        g=1
    elif(y==2*x-2):
        c=b
        y+=b
        z=2*x+1
    else:
        break
a=0
i=0
while(i<x**2):
    print(l[i],end=" ")
    if(i==x+a-1):
        print()
        a+=4
    i=i+1
        
        
    
