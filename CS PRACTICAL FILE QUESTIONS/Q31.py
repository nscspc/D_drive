import pickle
x=int(input("How many Students details you want to enter : "))
y=0
while(y<x):
    #pickle.dump("\b",file)
    srno=int(input("Enter srno. of Student : "))
    name=input("Enter name of Student : ")
    marks=int(input("Enter Marks : "))
    dicty={"SrNo.":srno,"Name":name,"Marks":marks}
    file=open("e:\\Q31(R 1).dat","ab")
    pickle.dump("\b",file)
    pickle.dump(dicty,file)
    y=y+1
pickle.dump("    ",file)
file.close()

print("Data added successfully")
