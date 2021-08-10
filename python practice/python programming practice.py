x=int(input("enter limit : "))
m=2
flag=0
y=2
while(y<=x):
    m=2
    while(m<=y/2):
        if(y%m==0):
            flag=flag+1
        m=m+1
    #y=y+1
    
    if(flag==0):
        print(y)
      #  print(y,"is not a prime number as it has",flag,"factors other then 1 and self")
    #else:
      #  print(y,"is a prime number")
    flag=0
    y=y+1
