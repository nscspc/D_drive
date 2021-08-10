string=input("Enter the Characters : ")
a,d,an,u,l,s,sy=0,0,0,0,0,0,0
length=len(string)
ch=0
i=0
while(ch<length):
    if string[i].isalnum():
        an+=1
    if string[i].isalpha():
        a+=1
        if string[i].islower():
            l+=1
        if string[i].isupper():
            u+=1
    elif string[i].isdigit():
        d+=1
    elif string[i].isspace():
        s+=1
    else:
        sy+=1
    ch+=1
    i+=1
if a!=0:
    print("No. of Alphabets are :",a)
if d!=0:
    print("No. of Digits are :",d)
if an!=0:
    print("No. of AlphaNumeric characters are :",an)
if sy!=0:
    print("No. of symbols are :",sy)
if u!=0:
    print("No. of Uppercase letters are :",u)
if s!=0:
    print("No. of Spaces are :",s)
if l!=0:
    print("No. of  Lowercase letters are :",l)
