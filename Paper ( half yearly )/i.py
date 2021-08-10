def countmy():
    file=open("e:\\DATA.txt","r")
    c=0
    while str:
        str=file.readline()
        if str=="my":
            c=c+1
    print(c)
    file.close()
