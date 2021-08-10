import pickle

file=open("e:\\pickle.txt","wb")

list1=[10,20,30,40,10000]

pickle.dump(list1,file)

print("Data Added SUCCESSFULLY")

file.close()
