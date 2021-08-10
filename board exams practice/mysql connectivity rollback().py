import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="school")
mycursor=mydb.cursor()
nm=input("enter name of the student whose record is to be deleted : ")
try:
    mycursor.execute("delete from student where name='b'")
    mycursor.execute("delet from student where name='"+nm+"'")
    print(mycursor.rowcount,"records deleted")
    mydb.commit()
except:
    mydb.rollback()
    print("rollbacked")
mydb.close()
'''rollback():-this function is used to revert the action done
    by the exeecuted query if there is error in the mysql query
    due to which runtime error occurs(runtime error occurs due to syntax error).
    like there is an error in 2nd query in which there is 'delet' instead of 'delete'
    so all changes done will be reverted'''
