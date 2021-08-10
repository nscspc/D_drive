file=open("e:\\read.txt","r")
file.read(2)
lines=file.readlines(20)
for line in lines:
    print(line,end="")
print("'")
print(file.read())
