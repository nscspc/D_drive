file=open("e:\\Q30.txt","r")
c=0
x=0
while str:
    str=file.read(1)
    c=c+1
    if str==" " or str=="\n":
        x=x+1
        
print(c-1-x)
