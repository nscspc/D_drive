d={"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10"}
user=input("enter username : ")
passwd=input("enter password : ")
flag=0
flagji=0
for keys in d:
    if user==keys:
        flag=1
        break
if flag==1:
    if passwd==d[user]:
        flagji=1

if flag==1 and flagji==1:
    print("you are now logged into the system")
if flag!=1:
    print("you are not a valid user of the system")
if flag==1 and flagji!=1:
    print("password is invalid")
