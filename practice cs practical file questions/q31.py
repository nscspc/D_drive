import pickle
rnos=int(input("Enter Roll no. : "))
names=input("Enter Name : ")
marks=int(input("Enter Marks : "))
l=[rnos,names,marks]
file=open("marks.dat","wb")
pickle.dump(l,file)
file.close()
