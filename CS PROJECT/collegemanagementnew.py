import mysql.connector as my


def selection():
    print("STUDENT ZONE")
    print("1.Login")
    print("2.Signup")
    print("3.Deactivate account")
    print("4.Teacher's appraisal")
    
    print(" ")
    print(" ")

    print("TEACHER's LOGIN")
    print("a.)Login")

    print(" ")
    print(" ")

    print("ADMINISTRATION LOGIN")
    print("b.)login")


def login():    #student login function
    
    use=input("enter your username")
    paswd=input("enter your passwd")
    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT Password from credentials where Username='"+use+"'")
    row=mycursor.fetchall()
    for i in row:
        if i[0]==paswd:
            print("You are logged in")
            
            assk="y"
            while assk=="y":
                print("1.)B.Tech student result")
                print("2.)Commerce student result")
                ask1=int(input("enter your response"))
                if ask1==1:
                    r1=str(input("Enter your Rollno."))
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    print("The marks in Physics,Maths are:")
                    mycursor.execute("SELECT Physics,Maths from  btechresult where Rollno="+r1+"")
                    for i in mycursor:
                        print(i)
                        
                        print("Do you want to see another result y/n")
                        assk=input("enter your response")
	                

                elif ask1==2:
                    assk="y"
                    r2=input("Enter your Rollno.")
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    print("The marks in BST,Accountancy,Economics are:")
                    mycursor.execute("SELECT BST,Accountancy,Economics from comresult where Rollno="+r2+"")
                    for j in mycursor:
                        print(j)
                        
                        print("Do you want to see other result y/n")
                        assk2=input("enter your response")
                        if assk2=="n":
                            manifun()

                        
            else:
                print("Invalid access",)
                manifun()


def signup():    #student signup function
    
    e="y"
    while e=="y":
        u1=input("Enter the username you want to set")
        p1=input("Enter the password you want to set")
        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO credentials values('"+u1+"','"+p1+"')")
        mydb.commit()
        print("You are registered in our system")
        
        assk2=input("Do you want to continue y/n")
        if assk2=="n":
            manifun()


def accdeacti():    #function of deactivating account of student
    
    f="y"
    while f=="y":
        u2=input("Enter your current Username")
        p2=input("Enter your current Password")
        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM credentials where Username='"+u2+"'")
        mydb.commit()
        print("Your id has been deactivated")
        
        assk3=input("Do you want to continue y/n")
        if assk3=="n":
            manifun()


def teachapp():    #funtion of teacher's appraisal
    
    print("Press e to continue as btech student")
    print("Press c to continue as commerce student")
    
    kj=input("enter your choice")
    
    if kj=="e":
        rono=input("Enter your roll no")
        phygrade=input("Enter the grade in physics")
        chemGrade=input("Enter the grade in chemistry")
        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO Teachersappraisalbtech values('"+rono+"','"+phygrade+"','"+chemGrade+"')")
        mydb.commit()
        print("You have successfully done the appraisal")
        
        manifun()

    elif kj=="c":
        rono1=input("Enter your roll no")
        BSGrade=input("Enter the grade in BST")
        Accgrade=input("Enter the grade in Accounts")
        Ecgrade=input("Enter the grade in Economics")
        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
        mycursor=mydb.cursor()
        mycursor.execute("INSERT INTO Teachersappraisalcoms values('"+rono1+"','"+BSGrade+"','"+Accgrade+"','"+Ecgrade+"')")
        mydb.commit()
        print("You have successfully done the appraisal")
        
        manifun()


def tlogin():    #teacher login function
    
    u4=input("Enter your Username")
    p4=input("Enter your Password")
    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT Password from Teachercred where Username='"+u4+"'")
    row1=mycursor.fetchall()
    for i in row1:
        if i[0]==p4:
            print("Access Granted")
            print("c.)Enter c to grade students")
            print("d.)Enter d to enter result of new btechstudents")
            print("e.)Enter e to enter result of commerce students")
            re=input("enter your response")
            if re=="c":
                assk5="y"
                while assk5=="y":
                    rn=input("Enter roll no of student whom you want to grade")
                    ss=input("Enter the grade in Speakingskills")
                    ps=input("Enter the grade in Personality")
                    ac=input("Enter the grade in Academics")
                    ph=input("Enter the grade in Personal hygiene")
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("UPDATE studentassessment set SpeakingSkills='"+ss+"', Personality='"+ps+"', Academics='"+ac+"', Personalhygiene='"+ph+"' where Rollno='"+rn+"'")
                    mydb.commit()
                    print("The student has been graded")
                    
                    assk5=input("Do you want to continue y/n")
                    if assk5=="n":
                        manifun()
            
                
            elif re=="d":
                assk6="y"
                while assk6=="y":
                    rn1=input("Enter the rollno of student whom result you want to add")
                    nm=input("Enter the name of student")
                    ph=input("Enter the marks in physics")
                    ma=input("Enter the marks in Mathematics")
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("INSERT INTO btechresult values('"+rn1+"','"+nm+"','"+ph+"','"+ma+"')")
                    mydb.commit()
                    print("The table has been updated")
                    
                    assk6=input("Do you want to continue y/n")
                    if assk6=="n":
                        manifun()

            elif re=="e":
                assk7="y"
                while assk7:
                    rn2=input("Enter the rollno of student whom result you want to add")
                    nm1=input("Enter the name of student")
                    bs=input("Enter the marks in BST")
                    ac=input("Enter the marks in accountancy")
                    ec=input("Enter the marks in economics")
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("INSERT INTO comresult values('"+rn2+"','"+nm1+"','"+bs+"','"+ac+"','"+ec+"')")
                    mydb.commit()
                    print("The table has been updated")
                    
                    assk7=input("Do you want to continue y/n")
                    if assk7=="n":
                        manifun()

                    
    else:
        print("Invalid Credentials")
        tlogin()
        

def adlo():    #administration login function
    
    Use2=input("enter your username")
    pas2=input("enter your password")
    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT Password from adcred where Username='"+Use2+"'")
    
    for i in mycursor:
        if i[0]==pas2:
            print("Access Granted")
            
            print("Enter t to view student's detail")
            print("Enter g to add new student in the school record")
            print("Enter h to view the Details of teachers")
            print("Enter w to add details of New teacher")
            print("Enter x to create USERNAME & PASSWORD of New Teacher")
            print("Enter f to display Fee Structure")
            
            re2=input("Enter your response")
            
            if re2=="t":
                c="y"
                while(c=="y"):
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("SELECT * FROM studentprofile")
                    
                    print("Roll No."," ","Name"," "," ","Fathers Name"," "," ","Mothers Name"," "," ","Address"," ","PhoneNo."," ","City"," ","FeeStatus")

                    for i in mycursor:
                        if i!=" ":
                            print(i)
                        else:
                            print("empty")
                            
                    assk9=input("Do you want to view data again y/n")
                    if assk9=="n":
                        manifun()
                    else:
                        c="y"
                    
                    
            elif re2=="g":
                z="y"
                while z=="y":    
                    Rno=input("Enter the  rollno")
                    Na=input("Enter the Name")
                    Fathna=input("Enter the Fathers name")
                    MotherNa=input("Enter the mothers name")
                    Add=input("Enter the address")
                    Phon=input("Enter the PhoneNo.")
                    Ci=input("Enter the city")
                    Feestat=input("Enter the fee status in dep(deposited) or rem(remaining)")
                    
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("INSERT INTO studentprofile values('"+Rno+"','"+Na+"','"+Fathna+"','"+MotherNa+"','"+Add+"','"+Phon+"','"+Ci+"','"+Feestat+"')")
                    mydb.commit()
                    print("New Record Successfully Inserted")
                    
                    assk10=input("Do you want to enter more details y/n")
                    if assk10=="n":
                        manifun()
                        
                        

            elif re2=="h":
                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("SELECT * FROM Teacherdetail")
                    
                    print("Name","   ","   ","Post","  "," ","Phoneno","  ","Salary"," ")
                    
                    for i in mycursor:
                        if i!="  ":
                            print(i)
                        else:
                            print("empty")
                    manifun()


            elif re2=="w":

                c="y"

                while(c=="y"):
                    print("Enter the Details of New Teacher : ")
                    name=input("Enter Name of the teacher : ")
                    post=input("Enter Post of the teacher : ")
                    phno=input("Enter Phone No. of the teacher : ")
                    salary=input("Enter Salary of the teacher : ")

                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("insert into teacherdetail values('"+name+"','"+post+"','"+phno+"','"+salary+"')")
                    mydb.commit()
                
                    print("Details Added Successfully")
                    
                    a=input("do you want to enter details of more teacher (y/n) : ")
                    if a=="y":
                        c="y"
                    else:
                        manifun()


            elif re2=="x":

                c="y"

                while(c=="y"):
                    un=input("Enter the USERNAME of the teacher : ")
                    ps=input("Enter the Login Password : ")

                    mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                    mycursor=mydb.cursor()
                    mycursor.execute("insert into teachercred values('"+un+"','"+ps+"')")
                    mydb.commit()
                
                    print("Teacher's Account created successfully")

                    a=input("do you want to enter details of more teacher (y/n) : ")
                    if a=="y":
                        c="y"
                    else:
                        manifun()

            elif re2=="f":

                c="y"

                while(c=="y"):
                    print("Of which stream do you want to see fee_structure :")
                    print("1.) BTECH")
                    print("2.) COMMERCE")
                
                    cf=input("Enter your choice : ")

                    if cf=="1":
                        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from btech_fee_structure")

                        for i in mycursor:
                            print(i)

                        a=input("do you want to see fee structure again ? (y/n) : ")
                        if a=="y":
                            c="y"
                        else:
                            manifun()

                    elif cf=="2":
                        mydb=my.connect(host="localhost",user="root",passwd="naveen",database="college")
                        mycursor=mydb.cursor()
                        mycursor.execute("select * from com_fee_structure")

                        for i in mycursor:
                            print(i)

                        a=input("do you want to see fee structure again ? (y/n) : ")
                        if a=="y":
                            c="y"
                        else:
                             manifun()

                    else:
                        print("invalid input")
                        manifun()
              
        else:
            print("Invalid access")
            manifun()
            
            
        
        
#MAIN DRIVER CODE
            

def manifun():

    selection()
    
    dd=input("enter your response")
    
    if dd=="1":
        login()
    elif dd=="2":
        signup()
    elif dd=="3":
        accdeacti()
    elif dd=="4":
        teachapp()
    elif dd=="a":
        tlogin()
    else:
        adlo()
        
    
manifun()
