d={"Naveen":"n@1*","Ramit":"mitra1","Vishesh":"shesh45","Harsh":"har54","Manish":"nish8888","Rohit":"hitro17","Siddharth":"sid1040","Shubham":"'bham100","Aditya":"aadi654","Shivam":"shi100"}

x=input("Enter your USERNAME :")
y=input("Enter PASSWORD :")
fact=0

for keys in d:
    if x==keys:
        fact=1

if fact==0:
    print("you are not a valid user of the system")
elif fact==1:
    if y!=d[x]:
        print("the password is invalid")
    else:
        print("you are now logged into the system")
