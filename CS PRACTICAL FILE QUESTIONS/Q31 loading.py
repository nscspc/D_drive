import pickle
file=open("e:\\Q31(R 1).dat","rb")
c="y"
while(c=="y"):
    dict1=pickle.load(file)
    if dict1!="   ":
        print(dict1)
        c="y"
    else:
        c="n"
file.close()
print()
