file=open("e:\\Q29.txt","r")
file2=open("e:\\Q29(R).txt","a")
c=0
while str:
    str=file.readline()
    x=str[0:1]
    if x=="p" or x=="P":
        file2.write(str)

file.close()
file2.close()
print("data added successfully")
