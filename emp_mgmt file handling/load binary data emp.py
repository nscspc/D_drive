import pickle
file=open("e:\\empmgmt.dat","rb")
x=0
while(x<3):
    dict1=pickle.load(file)
    print(dict1,end=" ")
    x=x+1
file.close()
print()
