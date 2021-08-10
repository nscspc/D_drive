file=open("e:\\sps.txt","r")
c=0
while str:
    str=file.readline()
    #if str!=" ":
    c=c+1
    print(str)
print(c-1)
