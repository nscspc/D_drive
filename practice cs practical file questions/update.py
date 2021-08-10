import mysql.connector as my

mydb=my.connect(host='localhost',user='root',password='manager',database='cs')
mycursor=mydb.cursor()
mycursor.execute('update salary set staffid=366 where staffid=336')
mydb.commit()
print('data updated successfully')
