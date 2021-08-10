file=open("e:\\tot5.txt","r")
c=0
a=0
x=0
while(x<=12):
    a=file.readline()
    for i in range(0,50):
   #     int=file.readline()
        if int(a)==i:
            c=c+1
    x+=1
    print(a)
    print(type(a))
print(c)
