import pickle
file=open('marks.dat','rb')
l1=pickle.load(file)
print(l1)
file.close()
