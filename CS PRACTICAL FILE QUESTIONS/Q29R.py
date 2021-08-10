f1=open("e:\\Q29.txt","r")
f2=open("e:\\Q29r.txt","w")

while str:
    str=f1.readline()
    x=str[0:1]
    if x=="p" or x=="P":
        f2.write(str)

f1.close()
f2.close()
