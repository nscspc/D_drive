file=open("q30.txt","r")
c=0
while str:
    str=file.read(1)
    if str==" " or str=="\n":
        c=c+1
print(c)
