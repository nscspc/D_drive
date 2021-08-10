str1=input("enter string : ")
str2=""
#for i in range(0,len(str1)):
for i in str1:
    str2=i+str2;
if(str1==str2):
    print('string is pallindrome')
else:
    print("string is not a pallindrome")
