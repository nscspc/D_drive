f=open("e:\\k.txt","r")
file=open("e:\\kw.txt","w")
while str:
    str=f.readline()
    if str[0:1]=="p" or str[0:1]=="P":
        file.write(str)
        
f.close()
file.close()
