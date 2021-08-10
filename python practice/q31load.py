import pickle
f=open("file.dat","rb")
c=0
while str:
    str=f.read()
    c+=1
f.close()
f=open("file.dat",'rb')
print("c=",+c)
for i in range(0,c):
    l=pickle.load(f)
    print(l)
f.close()
