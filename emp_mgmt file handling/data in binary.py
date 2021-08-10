import pickle

no=0

def add():
    file=open("e:\\empmgmt.dat","wb")
    x=0
    l=int(input("enter no. of records you want to enter : "))
    while(x<l):
        eid=int(input("enter id : "))
        name=input("enter name : ")
        sal=int(input("enter salary : "))
        pickle.dump(eid,file)
        pickle.dump(name,file)
        pickle.dump(sal,file)
        pickle.dump("#",file)
        
        x=x+1
        file.close()
        no=no+1
        print("data added successfully")

def show():
    import pickle
    file=open("e:\\empmgmt.dat","rb")
    x=0
    while(x<no):
        dict1=pickle.load(file)
        if dict1=="#":
            x=x+1
        else:
            print(dict1,end=" ")
    file.close()
    print()

    
