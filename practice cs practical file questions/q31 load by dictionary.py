import pickle
file=open('marks1.dat','rb')
var=True
while(var==True):
    l1=pickle.load(file)
    if l1!="/n":
        print(l1)
        var=True
    else:
        var=False
file.close()
