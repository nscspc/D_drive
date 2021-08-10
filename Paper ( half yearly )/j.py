def countmy():
    file=open("e:\\DATA.txt","r")
    c=0
    x=file.read()
    words=x.split()
    for i in words:
        if i=="my":
            c=c+1
    print(c)
    file.close()
