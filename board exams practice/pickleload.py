import pickle
f=open("e:\\picdum.txt","rb")
a=pickle.load(f)
print(a)
f.close()
#f.close() is not necessary
