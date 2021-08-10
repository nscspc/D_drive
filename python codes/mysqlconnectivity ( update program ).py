import mysql.connector as my

mydb=my.connect(host="localhost",user="root",passwd="naveen",database="ss")
mycursor=mydb.cursor()
mycursor.execute("update staff set department='Research' where name='krishna'")
mydb.commit()

print("Data Updated Successfully")

