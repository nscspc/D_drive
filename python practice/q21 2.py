dcon={}
n=int(input("enter no. of country details you want to enter : "))
for i in range(0,n):
    cn=input("enter name of country : ")
    ccap=input("enter capital of country : ")
    ccur=input("enter currency : ")

    dcon[cn]=[ccap,ccur]
print(dcon)
print("country name     capital     currency\n")
for keys in dcon:
    print("   ",keys,"           ",dcon[keys][0],"              ",dcon[keys][1])
