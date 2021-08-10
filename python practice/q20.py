dicty={'naveen':'pass'}
fact=0
username=input("enter username:")
password=input("enter password : ")
for values in dicty:
    print(dicty[values])
for k in dicty:
    if(k==username):
        fact=1
        break
if(fact==1):
    if(password==dicty[k]):
        print("you are now logged in ")
    else:
        print("wrong password")
else:
    print("you are not a valid user")
