def fibonacci(n,a=0,b=1,c=0):
    if n==0:
        return None
    elif n==1:
        if c==0:
            return a
        else:
            print(",",b,end=" ")
    else:
        if a==0:
            print(a,",",b,end=" ")
            return fibonacci(n-2,a=b,b=a+b,c=c+1)
        else:
            print(",",b,end=" ")
            return fibonacci(n-1,a=b,b=a+b,c=c+1)
