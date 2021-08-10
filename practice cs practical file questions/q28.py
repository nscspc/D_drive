file=open("q28.txt","r")
l=['a','e','i','o',"u",'A','E','I','O','U']
c=0
while str:
    str=file.read(1)
    for i in l:
        if str==i:
            c=c+1
            continue#time decreased
print(c)
