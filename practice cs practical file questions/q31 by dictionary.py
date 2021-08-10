import pickle
no=int(input("Enter the no. of STUDENTS whose Data you want to add : "))
file=open("marks1.dat","ab")
for i in range(0,no):
    rnos=int(input("Enter Roll no. : "))
    names=input("Enter Name : ")
    marks=int(input("Enter Marks : "))
    d={"rnos":rnos,"names":names,"marks":marks}
    pickle.dump(d,file)
pickle.dump("/n",file)
file.close()
print("Data Added Successfully")
