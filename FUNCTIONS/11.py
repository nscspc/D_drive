file=open("e:\\sps.txt","r")
c=1
while str:
    str=file.readline(1)
    if str==" " or str=="/n":
        c=c+1
print(c)
