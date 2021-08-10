dcon={country_name{}}
n=int(input("enter no. of country details you want to enter : "))
for i in range(0,n):
    dcon["country_name"]=input("enter name of country : ")
    country_name["capital"]=input("enter capital of country : ")
    country_name["currency"]=input("enter currency of '"+con+"' : ")

print(dcon)
