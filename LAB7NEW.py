import mysql.connector
cnx=mysql.connector.connect(host='localhost',port=3306,user='root',password='',database='lab_assignment1')
cursor=cnx.cursor(buffered=True)
cursor.execute('SHOW TABLES')
for x in cursor:
    print(x)