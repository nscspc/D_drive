import hashlib

string=input("enter string that you want to encrypt : ")
s=string.encode()#string should be encoded before hashing
print("encrypted form of",string,"in md5 is :",hashlib.md5(s).hexdigest())
