import hashlib

string=input("enter string that you want to encrypt : ")
print("choose the algorithm in which you want to encrypt the string : \n(1). md5\n(2). sha1\n(3). sha512")
algo=int(input("enter you choice here : "))
s=string.encode()# string should be encoded before hashing

if(algo==1):
    print("encrypted form of",string,"in md5 is :",hashlib.md5(s).hexdigest())
elif(algo==2):
    print("encrypted form of",string,"in sha1 is :",hashlib.sha1(s).hexdigest())
elif(algo==3):
    print("encrypted form of",string,"sha512 is :",hashlib.sha512(s).hexdigest())
else:
    print("wrong input")
