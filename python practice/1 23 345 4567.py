c=1
n=int(input("enter no. of rows of pattern : "))
for i in range(1,n+1):
    for j in range(i,i+c):
        print(j,end=" ")
    print()
    c+=1
        
