m=2
x=5
flag=0
while(m<=x):
    if x%m==0:
        flag=1
    m=m+1
    if flag==0:
    	print(x)
    if flag==1:
        print()
        x=x+1
