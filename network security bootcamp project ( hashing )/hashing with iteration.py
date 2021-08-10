import hashlib

string=input("enter string that you want to encrypt : ")
print("choose the algorithm in which you want to encrypt the string : \n(1). md5\n(2). sha1\n(3). sha512")
algo=int(input("enter you choice here : "))
s=string.encode()# string should be encoded before hashing
hashed=s
if(algo==1):
    for i in range(10):
        s=hashlib.md5(s).hexdigest()
        s=s.encode()
    print("10 times hashed form of",string,"in md5 is :",s)
elif(algo==2):
    for i in range(10):
        s=hashlib.sha1(s).hexdigest()
        s=s.encode()
    print("10 times hashed form of",string,"in sha1 is :",s)
elif(algo==3):
    for i in range(10):
        s=hashlib.sha512(s).hexdigest()
        s=s.encode()
    print("10 times hashed form of",string,"in sha512 is :",s)
else:
    print("wrong input")
