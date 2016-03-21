#! /usr/bin/python

import cgi
import mysql.connector as conn

def htmlTop():
	print """Content-Type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>MATRIX LOCATION CHAT DB</title>
				<body>"""

def connectDB():
	db = conn.connect(host='localhost',port=8889,user='root',passwd='root')
	cursor = db.cursor()
	return db,cursor

def createDB(db,cursor):
	#creating a new database
	sql = "create database matrixdb"
	cursor.execute(sql)
	db.commit()

def createEntity(db,cursor):
	#use the newly created database
	sql = "use matrixdb"
	cursor.execute(sql)
	#create a simple entity
	sql = '''create table chatroom
	(id int not null auto_increment,
	roomname varchar(20),
	roomowner varchar(30),
	participants varchar(200)
	roomlat float,
	roomlong float)'''

	cursor.execute(sql)
	db.commit()

	
def htmlTail():
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		createDB(db,cursor)
		createEntity(db,cursor)
		#close the connection
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()				