f1=open("q29.txt","r")
f2=open("q29w.txt","w")
while str:
    str=f1.readline()
    x=str[0:1]
    if x=="p" or x=="P":
        f2.write(str)
f1.close()
f2.close()
print("Data Added Successfullys")
