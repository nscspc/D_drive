file=open("e:\\sps.txt","r")
c=0
ch=" "
while ch:
    ch=file.readline(1)
    if ch==" " or ch=="/n":
        c=c+1
print(c)
