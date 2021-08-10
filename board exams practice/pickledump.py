import pickle
f=open("e:\\picdum.txt","wb")
l=[1,2,3,45,6,1,66]
pickle.dump(l,f)
print("data added successfully")
f.close()#f.close() is necessary
