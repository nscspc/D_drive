user={}

def signup():
    username=input("enter username : ")
    pswd=input("enter password : ")
    f_name=input("enter first name : ")
    l_name=input("enter last name : ")
    age=int(input("enter your age : "))
    gender=input("enter gender (M/F/O) : ")
    to=input("to whom you want to send the msg : ")
    msg=input("enter your message : ")

    user[username]={'password':pswd,'fname':f_name,'lname':l_name,'age':age,'gender':gender,'msg':msg}

    print("these are the details entered by you : ")
    for i,j in user.items():
        print(i)
        for k in j: 
            print('\t',k,'=',j[k])

    choice=input("do you want to edit it (y/n) : ")
    if(choice=='y' or choice=='Y'):
        edit=input("what do you want to edit : \n press p for password \n press f for firstname \n press l for lastname \n press a for age \n press g for gender \n press m for msg \n: ")
        if()


def signin():
    username=input("enter your name : ")
    pswd=input("enter password : ")

    for i,j in user.items():
        if(i==username):
            if(j['password']==pswd):
                print("you are signed in successfully")
            else:
                print("you entered wrong password")
                again=input("do you want to enter again : ")
                if(again=='y' or again=='Y'):
                    signin()

        else:
            print("you entered wrong username")
            again=input("do you want to enter again : ")
                if(again=='y' or again=='Y'):
                    signin()
