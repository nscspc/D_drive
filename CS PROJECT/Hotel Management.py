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
        con=my.connect(host="localhost",user="root",passwd="naveen",database="hotel")
        cur=con.cursor()
        cur.execute("select passwd,user_n  from cred where user_n='"+uname+"'")
        row=cur.fetchall()
        for r in row:
            if r[0]==pswd:
                print("Sucessfully Login!")
                cur.close()
#                !!!hotel functions!!!
                f0="n"
                while f0=="n":
                    print("""
---1-Employee Details---
---2-Menu Functions---
---3-Stock Details---
---4-Update Or Delete LoginID And Password---
---0-LOGOUT---""")
                    a=input("ENTER:-")
                    if a=="1":
#                        !!!employee details functions!!!
                        f1="n"
    
                        while f1=="n":
                            print("")
                            print("---1-All Staff Details---")
                            print("---2-Search Employee By E_ID---")
                            print("---3-Change Employee Details---")
                            print("---4-Add New Employee---")
                            print("---5-Delete Employee Details---")
                            print("---0-Exit Staff Functions---")
                            a1=input("ENTER:-")
#                            !!!all details!!!
                            if a1=="1":
                                con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                cur.execute("select * from staff")
                                for i in cur:
                                    print(i)
                                con.close()
#                            !!!searcher!!!
                            if a1=="2":
                                y="y"
                                while y=="y":
                                    eid=input("Enter Employee ID:-")
                                    con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                    cur=con.cursor()
                                    cur.execute("select * from staff where s_id='"+eid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Invalid Id!")
                                    else:
                                        cur.execute("select * from staff where s_id='"+eid+"'")
                                        for i in cur:
                                            print(i)
                                        con.close()
                                        y=input("Search Another Id(y/n):-")
                                       
                                       
#                            !!!changer!!!
                            if a1=="3":
                                con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                eid=input("Enter Employee ID:-")
                                cur.execute("select * from staff where s_id='"+eid+"'")
                                x=cur.fetchone()
                                if x==None:
                                    print("Invalid Id!")
                                else:
                                    print("""
---1-Change name---
---2-Change Contact---
---3-Change Address---
---4-Change Salary---""")
                                    a10=input("ENTER:-")
                                    if a10=="1":
                                        aq=input("Enter New Name:-")
                                        con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_name='"+aq+"' where s_id='"+eid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="2":
                                        aq=input("Enter New Contact:-")
                                        con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_phone='"+aq+"' where s_id='"+eid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="3":
                                        aq=input("Enter New Address:-")
                                        con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_addr='"+aq+"' where s_id='"+eid+"'")
                                        con.commit()
                                        con.close()
                                        print("Record Updated!")
                                    if a10=="4":
                                        aq=input("Enter New Salary:-")
                                        con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("update staff set s_salary='"+aq+"' where s_id='"+eid+"'")
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
                                con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                cur.execute("select s_id from staff where s_id='"+nid+"'")
                                x=cur.fetchone()
                                if x==None and len(nap)<=11:
                                    cur.execute("insert into staff values('"+str(nid)+"','"+nna+"','"+nad+"','"+nap+"','"+nsa+"','"+npo+"')")
                                    con.commit()
                                    con.close()
                                    print("Details Saved!")
                                else:
                                    print("ID Already Exists Or Invalid Contact!")
#                            !!!remover!!!
                            if a1=="5":
                                aw=input("Enter Employee ID:-")
                                con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                cur.execute("select * from staff where s_id='"+aw+"'")
                                x=cur.fetchone()
                                if x==None:
                                     print("Invalid Id!")
                                else:
                                    cur.execute("delete from staff where s_id='"+aw+"'")
                                    con.commit()
                                    con.close()
                                    print("Record Removed!")
                                  
                            if a1=="0":
                                f1="y"
                                print("Staff Functions Closed!")
#                        !!!Menu Functions!!!
                    if a=="2":
                        f1="n"
                        while f1=="n":
                            print("""
---1-See Menu---
---2-Search Item---
---3-Add Item---
---4-Remove Item---
---5-Update Item---
---0-Exit Menu---""")
                            a2=input("ENTER:-")
#                            !!!see menu!!!
                            if a2=="1":
                                con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                cur.execute("select * from menu")
                                for i in cur:
                                    print(i)
#                            !!!search item!!!
                            if a2=="2":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                    cur=con.cursor()
                                    a=input("Enter Item Code:-")
                                    cur.execute("select * from menu where i_code='"+a+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Invalid Id!")                                       
                                    else:
                                        cur.execute("select * from menu where i_code='"+a+"'")
                                        for i in cur:
                                            print(i) 
                                        ad=input("Search Other Item(y/n):-")
                                        
#                            !!!Add item!!!
                            if a2=="3":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    ico=input("Enter Item code:-")
                                    ina=input("Enter Item Name:-")
                                    ipa=int(input("Enter Item Price:-"))
                                    con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                    cur=con.cursor()
                                    cur.execute("select * from menu where i_code='"+ico+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Try Again!")                                        
                                    else:
                                        cur.execute("insert into menu values('"+ico+"','"+ina+"','"+str(ipa)+"')")
                                        print("Sucessfully Added!")
                                        con.commit()
                                        con.close()
                                        ad=input("Add Other Item(y/n):-")
                                        print("Item code Already Exists!")
                                       
#                            !!!remover!!!
                            if a2=="4":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                    cur=con.cursor()
                                    a=input("Enter Item Code:-")
                                    cur.execute("select * from menu where i_code='"+a+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Invalid Id!")                                                                                                                        
                                    else:
                                        cur.execute("delete from menu where i_code='"+a+"'")
                                        con.commit()
                                        con.close()
                                        ad=input("Remove Other Item(y/n):-")
                                        print("Deleted Sucessfully!")
                                        
#                            !!!updater!!!
                            if a2=="5":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    print("""
---1-Change Item Name---
---2-Change Item Price---""")
                                    i=input("ENTER:-")
                                    if i=="1":
                                        e="y"
                                        while e=="y" or e=="Y":
                                            a=input("Enter Item Code:-")
                                            na=input("Enter New Name:-")
                                            con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                            cur=con.cursor()
                                            cur.execute("select * from menu where i_code='"+a+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Invalid Id!")                                                
                                            else:
                                                cur.execute("update menu set i_name='"+na+"' where i_code='"+a+"'")
                                                con.commit()
                                                con.close()
                                                e=input("Change Any Other Name(y/n):-")
            
                                    if i=="2":
                                        e="y"
                                        while e=="y" or e=="Y":
                                            a=input("Enter Item Code:-")
                                            na=int(input("Enter New price:-"))
                                            con=my.connect(host="localhost",user="root",passwd="naveen1234",database="hotel")
                                            cur=con.cursor()
                                            cur.execute("select * from menu where i_code='"+a+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Invalid Id!")                                                
                                            else:
                                                cur.execute("update menu set i_name='"+na+"' where i_code='"+a+"'")
                                                con.commit()
                                                con.close()
                                                e=input("Change Any Other Price(y/n):-")
                                                
                                    print("Record Updated!")
                                    ad=input("Change Any Other Record(y/n):-")
                            if a2=="0":
                                f1="y"
                                print("Menu Closed!")
                                
#                    !!!stock functions!!!
                    if a=="3":
                        qp="n"
                        while qp=="n":
                            print("""
---1-See List---
---2-Update Quantity---
---3-Remove Or Add Item---
---0-Exit Stock Functions---""")
                            a3=input("ENTER:-")
#                            !!!For list seeing!!!
                            if a3=="1":
                                con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
                                cur=con.cursor()
                                cur.execute("select * from stock")
                                for i in cur:
                                    print(i)
                                    
                                con.close()
                                    
#                            !!!Updater!!!
                            if a3=="2":
                                er="y"
                                while er=="y" or er=="Y":
                                    con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
                                    cur=con.cursor()
                                    ic=input("Enter Item Code:-")
                                    cur.execute("select * from stock where it_code='"+ic+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Invalid Code!")                                        
                                    else:
                                        upq=int(input("Enter New Quantity(in Kg):-"))
                                        cur.execute("update stock set it_quan_in_kg='"+str(upq)+"' where it_code='"+ic+"'")
                                        con.commit()
                                        con.close()
                                        print("Quantity Updated!")
                                        er=input("Change Any Other Quantity(y/n):-")
                                    
#                            !!!remover and adder!!!
                            if a3=="3":
                                ui="y"
                                while ui=="y" or ui=="Y":
                                    print("""---1-Add New Item---
---2-Remove Item---""")
                                    rty=input("ENTER:-")
                                    if rty=="1":
                                        df="y"
                                        while df=="y" or df=="Y":
                                            con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
                                            cur=con.cursor()
                                            itc=input("Enter Item Code:-")
                                            itn=input("Enter Item Name:-")
                                            itq=input("Enter Item Quantity(in Kg):-")
                                            cur.execute("select it_code from stock where it_code='"+itc+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                cur.execute("insert into stock values('"+itc+"','"+itn+"','"+itq+"')")
                                                con.commit()
                                                con.close()
                                                print("Item Added!")
                                            else:
                                                print("Item Code Already Exists!")
                                            df=input("Add Any Other Item(y/n):-")
                                                
                                    if rty=="2":
                                        op="y"
                                        while op=="y" or op=="Y":
                                            itc=input("Enter Item Code:-")
                                            con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
                                            cur=con.cursor()
                                            cur.execute("select it_code from stock where it_code='"+itc+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Invalid Item Code!")
                                            else:
                                                cur.execute("delete from stock where it_code='"+itc+"'")
                                                con.commit()
                                                con.close()
                                                print("Item Removed!")
                                            op=input("Remove Any Other Item(y/n):-")
                                            
                                    ui=input("Add Or Remove Any Other Item(y/n):-")
                            if a3=="0":
                                qp="y"
                                print("Stocks Closed!")
                    
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
                                            con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
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
                                            con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
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
                                    con=my.connect(host='localhost',user="root",passwd="naveen1234",database="hotel")
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
            con=my.connect(host="localhost",user="root",passwd="naveen",database="hotel")
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
