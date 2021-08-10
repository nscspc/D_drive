import pickle
rno=[]
name=[]
marks1=[]
marks2=[]
marks3=[]
rno.append(int(input("enter roll no. : ")))
name.append(input("enter roll no. : "))
marks1.append(int(input("enter roll no. : ")))
marks2.append(int(input("enter roll no. : ")))
marks3.append(int(input("enter roll no. : ")))
f=open("file.dat","ab")
#f.write(str(rno))
pickle.dump(rno,f)
pickle.dump(name,f)
pickle.dump(marks1,f)
pickle.dump(marks2,f)
pickle.dump(marks3,f)
f.close()
