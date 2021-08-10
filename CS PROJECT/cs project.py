import mysql.connector as my
yu="n"
while yu=="n":
    print("---1-FOR LOGIN---")
    print("---2-FOR SIGNUP---")
    print("---0-EXIT---")
    a6=input("ENTER:-")
    if a6=="1":
        uname=input("    ENTER USERNAME:-")
        pswd=input("    ENTER PASSWORD:-")
        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
        cur=con.cursor()
        cur.execute("select passwd,user_n  from cred where user_n='"+uname+"'")
        row=cur.fetchall()
        for r in row:
            if r[0]==pswd:
                print("Sucessfully Login!")
                cur.close()
#                !!!college management functions!!!
                f0="n"
                while f0=="n":
                    print("""
---1-Staff Details---
---2-student details---
---3-fee structure---
---4-Update Or Delete LoginID And Password---
---0-LOGOUT---""")
                    a=input("ENTER:-")
                    if a=="1":
#                        !!!staff details functions!!!
                        f1="n"
    
                        while f1=="n":
                            print("")
                            print("---1-All Staff Details---")
                            print("---2-Search By S_ID---")
                            print("---3-Change staff Details---")
                            print("---4-Add New member---")
                            print("---5-Delete staff Details---")
                            print("---0-Exit Staff Functions---")
                            a1=input("ENTER:-")
#                            !!!all details!!!
                            if a1=="1":
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select * from staff")
                                for i in cur:
                                    print(i)
                                con.close()
#                            !!!searcher!!!
                            if a1=="2":
                                y="y"
                                while y=="y":
                                    sid=input("Enter Member ID:-")
                                    con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                    cur=con.cursor()
                                    cur.execute("select * from staff where s_id='"+sid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Invalid Id!")
                                    else:
                                        cur.execute("select * from staff where s_id='"+sid+"'")
                                        for i in cur:
                                            print(i)
                                        con.close()
                                        y=input("Search Another Id(y/n):-")
                                       
                                       
#                            !!!changer!!!
                            if a1=="3":
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                choice=input("do you want to do change in few members(1) or do you want to do change in salary of all members(2):-")
                                if choice==1:
                                    sid=input("Enter Member ID:-")
                                    cur.execute("select * from staff where s_id='"+sid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Invalid Id!")
                                    else:
                                        print("""
---1-Change name---
---2-Change post---
---3-Change Salary---
---4-Change Contact---
---5-Change Address---
---6-Change e-mail---""")
                                        a10=input("ENTER:-")
                                        if a10=="1":
                                            aq=input("Enter New Name:-")
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_name='"+aq+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                        if a10=="2":
                                            ap=input("Enter New Post:-")
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_post='"+ap+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                        if a10=="3":
                                            ab=int(input("Enter New Salary:-"))
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_salary='"+int(ab)+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                        if a10=="4":
                                            ac=input("Enter New Contact:-")
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_phone='"+ac+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                        if a10=="5":
                                            aa=input("Enter New Address:-")
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_address='"+aa+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                        if a10=="6":
                                            ae=input("Enter New E-mail:-")
                                            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            cur.execute("update staff set s_salary='"+ae+"' where s_id='"+sid+"'")
                                            con.commit()
                                            con.close()
                                            print("Record Updated!")
                                if choice==2:
                                    s1=input("do you want to increase(1) or decrease(2):-")
                                    if s1==1:
                                        ab=input("Enter change in Salary:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_salary='"++int(ab)+"'")
                                        con.commit()
                                        con.close()
                                        print("salary increased by",ab)
                                    if s1==2:
                                        ab2=input("Enter change in Salary:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_salary='"-+int(ab)+"'")
                                        con.commit()
                                        con.close()
                                        print("salary decreased by",ab2)
                                
#                            !!!adder!!!
                            if a1=="4":
                                nid=input("Enter ID:-")
                                nna=input("Enter name:-")
                                nge=input("Enter gender:-")
                                npo=input("Enter post:-")
                                nsa=int(input("Enter Salary:-"))
                                nco=input("Enter contact:-")
                                nad=input("Enter address:-")
                                nel=input("Enter E-mail:-")

                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select s_id from staff where s_id='"+nid+"'")
                                x=cur.fetchone()
                                if x==None and len(nco)<=11:
                                    cur.execute("insert into staff values('"+str(nid)+"','"+nna+"','"+nge+"','"+npo+"','"+int(nsa)+"','"+nco+"','"+nel+"')")
                                    con.commit()
                                    con.close()
                                    print("Details Saved!")
                                else:
                                    print("ID Already Exists Or Invalid contact!")
#                            !!!remover!!!
                            if a1=="5":
                                am=input("Enter Member ID:-")
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select * from staff where s_id='"+am+"'")
                                x=cur.fetchone()
                                if x==None:
                                     print("Invalid Id!")
                                else:
                                    cur.execute("delete from staff where s_id='"+am+"'")
                                    con.commit()
                                    con.close()
                                    print("Record Removed!")
                                  
                            if a1=="0":
                                f1="y"
                                print("Staff Functions Closed!")
#                        !!!Student Functions!!!
                    if a=="2":
                        f1="n"
    
                        while f1=="n":
                            print("")
                            print("---1-All Students Details---")
                            print("---2-Search By Student_ID---")
                            print("---3-Change Student Details---")
                            print("---4-Add New Student---")
                            print("---5-Delete Student Details---")
                            print("---0-Exit Student Functions---")
                            a1=input("ENTER:-")
#                            !!!all details!!!
                            if a1=="1":
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select * from student")
                                for i in cur:
                                    print(i)
                                con.close()
#                            !!!searcher!!!
                            if a1=="2":
                                y="y"
                                while y=="y":
                                    sid=input("Enter Student ID:-")
                                    con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                    cur=con.cursor()
                                    cur.execute("select * from student where st_id='"+sid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Invalid Id!")
                                    else:
                                        cur.execute("select * from student where st_id='"+sid+"'")
                                        for i in cur:
                                            print(i)
                                        con.close()
                                        y=input("Search Another Id(y/n):-")
                                       
                                       
#                            !!!changer!!!
                            if a1=="3":
                                con=my.connect(host="localhost",user="root",passwd="n1234",database="cmg")
                                cur=con.cursor()
                                sid=input("Enter Student ID:-")
                                cur.execute("select * from student where st_id='"+sid+"'")
                                x=cur.fetchone()
                                if x==None:
                                    print("Invalid Id!")
                                else:
                                    print("""
---1-Change name---
---2-Change class---
---3-ChangeSubject---
---4-Change Contact---
---5-Change Address---
---6-Change E-MAIL---""")
                                    a10=input("ENTER:-")
                                    if a10=="1":
                                        an=input("Enter New Name:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update student set st_name='"+an+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="2":
                                        ac=input("Enter New class:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update student set st_class='"+ac+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="3":
                                        asb=input("Enter New Subject:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update student set st_subject='"+asb+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="4":
                                        aq=input("Enter New Contact:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update student set st_contact='"+aq+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="5":
                                        ad=input("Enter New Address:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update student set st_address='"+ad+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="6":
                                        ae=input("Enter New E-mail:-")
                                        con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                        cur=con.cursor()
                                        cur.execute("update staff set st_email='"+ae+"' where st_id='"+sid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                
#                            !!!adder!!!
                            if a1=="4":
                                nid=input("Enter ID:-")
                                nna=input("Enter name:-")
                                nad=input("Enter address:-")
                                nap=input("Enter Contact:-")
                                nsa=input("Enter Salary:-")
                                npo=input("Enter post:-")
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select st_id from student where st_id='"+nid+"'")
                                x=cur.fetchone()
                                if x==None and len(nap)<=11:
                                    cur.execute("insert into student values('"+str(nid)+"','"+nna+"','"+nad+"','"+nap+"','"+nsa+"','"+npo+"')")
                                    con.commit()
                                    con.close()
                                    print("Details Saved!")
                                else:
                                    print("ID Already Exists Or Invalid Contact!")
#                            !!!remover!!!
                            if a1=="5":
                                aw=input("Enter student ID:-")
                                con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                cur=con.cursor()
                                cur.execute("select * from student where st_id='"+aw+"'")
                                x=cur.fetchone()
                                if x==None:
                                     print("Invalid Id!")
                                else:
                                    cur.execute("delete from student where st_id='"+aw+"'")
                                    con.commit()
                                    con.close()
                                    print("Record Removed!")
                                  
                            if a1=="0":
                                f1="y"
                                print("Student Functions Closed!")
                        
#                    !!!fee structure!!!
                    if a==3:
                        f1="n"
                        while f1=="n":
                            print("")
                            print("---1-fee details---")
                            print("---2-change in fee---")
                            print("---0-Exit fee functions---")
                            a1=input("ENTER:-")
                            if a1==1:
                               con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                               cur=con.cursor()
                               cur.execute("select * from fee")
                               for i in cur:
                                   print(i)
                                   con.close()
                            if a1==2:
                                b1=input("do you want to increase(1) or decrease(2):-")
                                if b1==1:
                                    ab=input("Enter change in fee:-")
                                    con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                    cur=con.cursor()
                                    cur.execute("update fee set fee='"++int(ab)+"'")
                                    con.commit()
                                    con.close()
                                    print("fee increased by",ab)
                                if b1==2:
                                    ab2=input("Enter change in fee:-")
                                    con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
                                    cur=con.cursor()
                                    cur.execute("update fee set fee='"-+int(ab)+"'")
                                    con.commit()
                                    con.close()
                                    print("fee decreased by",ab2)

                            if a1==0:
                                f1="y"
                                print("fee function closed")

                                                
#                    !!!loginId or Password update or delete programme!!!
                    if a=="4":
                        lk="n"
                        while lk=="n" or lk=="N":
                            print("""
---1-For Updating LoginId Or Password---
---2-For Remove An ID---
---0-For Exit---""")
                            jkl=input("ENTER:-")
                            if jkl=="1":
                                ty="y"
                                while ty=="y":
                                    print("""
---1-Update LoginID---
---2-Update Password---""")
                                    rt=input("ENTER:-")
                                    if rt=="1":
                                        nm="y"
                                        while nm=="y" or nm=="Y":
                                            con=my.connect(host='localhost',user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            oid=input("Enter Old LoginID:-")
                                            nid=input("Enter New LoginID:-")
                                            cur.execute("select * from cred where user_n='"+oid+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Id Does not Exists!")                                                    
                                            else:
                                                cur.execute("update cred set user_n='"+nid+"' where user_n='"+oid+"'")
                                                con.commit()
                                                con.close()
                                                print("LoginID Updated!")
                                                nm=input("Change Any Other LoginID(y/n):-")
            
                                    if rt=="2":
                                        nm="y"
                                        while nm=="y" or nm=="Y":
                                            con=my.connect(host='localhost',user="root",passwd="1234",database="cmg")
                                            cur=con.cursor()
                                            oid=input("Enter LoginID:-")
                                            nid=input("Enter New Password:-")
                                            cur.execute("select * from cred where user_n='"+oid+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Id Does not Exists!")                                                
                                            else:
                                                cur.execute("update cred set passwd='"+nid+"' where user_n='"+oid+"'")
                                                con.commit()
                                                con.close()
                                                print("Password Updated!")
                                                nm=input("Change Any Other Password(y/n):-")
                                            
                                    ty=input("Change Any Other Login Or Password(y/n):-")
                                    
                            if jkl=="2":
                                nm="y"
                                while nm=="y" or nm=="Y":
                                    con=my.connect(host='localhost',user="root",passwd="1234",database="cmg")
                                    cur=con.cursor()
                                    oid=input("Enter LoginID:-")
                                    cur.execute("select * from cred where user_n='"+oid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Id Does not Exists!")                                       
                                    else:
                                        cur.execute("delete from cred where user_n='"+oid+"'")
                                        con.commit()
                                        con.close()
                                        print("LoginID Removed!")
                                        nm=input("Change Any Other Credential(y/n):-")
                                    
                            if jkl=="0":
                                lk="y"
                                print("Sucessfully Exit!")
              
                    if a=="0":
                        f0="y"
                        print("Sucessfully LOGOUT!")
                            
            else:
                print("Invalid Login Id or Password!")
                print("Try Again!!")
        
#    !!!Signup Function!!!            
    if a6=="2":
        y="y"
        while y=="y" or y=="Y":
            us=input("Enter New Username:-")
            ps=input("Enter New Password:-")
            con=my.connect(host="localhost",user="root",passwd="1234",database="cmg")
            cur=con.cursor()
            cur.execute("select * from cred where user_n='"+us+"'")
            x=cur.fetchone()
            if x==None:
                cur.execute("insert into cred values('"+us+"','"+ps+"')")
                print("Sucessfully Saved!")
                con.commit()
                con.close()
            else:
                print("UserID Already Exists!")
                
            y=input("Create Other New id(y/n):-")
#   !!!Programme Closer!!!  
    if a6=="0":
        yu="y"
        print("Programme Closed!")
