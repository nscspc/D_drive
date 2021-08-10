file=open(r"e:\sps.txt","r")
ch=" "
while ch:
    ch=file.readline()
    print(ch)
file.close()
