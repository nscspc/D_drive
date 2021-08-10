import mysql.connector as my

mydb=my.connect(host='localhost',user='root',password='manager',database='cs')
mycursor=mydb.cursor()
mycursor.execute('delete from staff where staffid=2')
mydb.commit()
print('data deleted successfully')
