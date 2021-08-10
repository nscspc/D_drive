string=input("Enter String : ")
l=len(string)-1
a,b,c,d,e,f,g=0,0,0,0,0,0,0
while(l>=0):
    if string[l].isalnum():
        c=c+1
    if string[l].isalpha():
        a=a+1
        if string[l].isupper():
            d=d+1
        if string[l].islower():
            e=e+1
    elif string[l].isdigit():
        b=b+1
    elif string[l].isspace():
        f=f+1
    else:
        g=g+1
    l=l-1
print(a,b,c,d,e,f,g)
        
