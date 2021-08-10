m=2
x=int(input("enter no."))
flag=0
while(m<=x/2):
    if x%m==0:
    	    flag=1
    m=m+1
    if flag==0:
    	    print("no, is prime")
    else:
	    print("no. is not prime")
	
