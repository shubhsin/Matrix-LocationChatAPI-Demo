#! /usr/bin/python

import cgi
import mysql.connector as conn

def htmlTop():
	print """Content-Type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>My server-side template</title>
				<body>"""

def connectDB():
	db = conn.connect(host='localhost',port=8889,user='root',passwd='root',db='matrixdb')
	cursor = db.cursor()
	return db,cursor

def displayRooms(db,cursor):
	sql = "select * from chatroom"
	cursor.execute(sql)
	#fetch the results as a list
	rooms = cursor.fetchall()

	print "<table border>"
	print "<tr>"
	print "<th>ID</th>"
	print "<th>Room Name</th>"
	print "<th>Room Owner</th>"
	print "<th>Participants</th>"
	print "<th>Room Latitude</th>"
	print "<th>Room Longitude</th>"
	print "</tr>"
	for each in rooms:
		print "<tr>"
		print "<td>{0}</td>".format(each[0])
		print "<td>{0}</td>".format(each[1])
		print "<td>{0}</td>".format(each[2])
		print "<td>{0}</td>".format(each[3])
		print "<td>{0}</td>".format(each[4])
		print "<td>{0}</td>".format(each[5])
		print "</tr>"
	print "</table>"
	
def htmlTail():
	print """</body>
		</html>"""


#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		displayRooms(db,cursor)
		htmlTail()
	except:
		cgi.print_exception()				