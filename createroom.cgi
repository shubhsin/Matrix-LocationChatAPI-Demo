#! /usr/bin/python

import cgi
import mysql.connector as conn

def htmlTop():
	print """Content-Type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>Create Room Page</title>
				<body>"""

def connectDB():
	db = conn.connect(host='localhost',port=8889,user='root',passwd='root',db='matrixdb')
	cursor = db.cursor()
	return db,cursor


def insertRoom(db,cursor):
	formData = cgi.FieldStorage()
	roomname = formData.getvalue('roomname')
	roomowner = formData.getvalue('roomowner')
	roomlat = formData.getvalue('roomlat')
	roomlong = formData.getvalue('roomlong')
	sql = "insert into chatroom(roomname,roomowner,roomlat,roomlong) values('{0}','{1}','{2}','{3}')".format(roomname,roomowner,float(roomlat),float(roomlong))
	cursor.execute(sql)
	db.commit()

	
def htmlTail():
	print """<h3>Successfully Created</h3>"""
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		insertRoom(db,cursor)
		#close the connection
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()				