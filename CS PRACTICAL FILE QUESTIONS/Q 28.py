name=input("enter name : ")
file=open("e:\\"+name+".txt","r")
str1=file.read()
vowels=['a','e','i','o','u','A','E','I','O','U']
l=len(str1)
v=len(vowels)
a,b,c,d=0,0,0,0
while(a<l):
    if b<l:
        for c in range(0,v):
            if str1[b]==vowels[c]:
                d=d+1
    if b<l:
        a=a+1
        b=b+1
        c=0
if d!=0:
    print(d)
else:
    print("No Vowel")

