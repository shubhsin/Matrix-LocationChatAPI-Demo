#! /usr/bin/python

import cgi
import mysql.connector as conn
import json

def htmlTop():
	print """Content-Type:application/json\n\n"""

def connectDB():
	db = conn.connect(host='localhost',port=8889,user='root',passwd='root',db='matrixdb')
	cursor = db.cursor()
	return db,cursor

def displayRooms(db,cursor):
	sql = "select * from chatroom"
	cursor.execute(sql)
	#fetch the results as a list
	rooms = cursor.fetchall()
	x = 0
	print "{\"data\":["
	for each in rooms:
		rmid = "{0}".format(each[0])
		roomname = "{0}".format(each[1])
		roomowner = "{0}".format(each[2])
		participants = "{0}".format(each[3])
		latitude = "{0}".format(each[4])
		longitude = "{0}".format(each[5])
		if x>0 :
			print ",{\"roomname\":\"" + roomname + "\","
		else :
			print "{\"roomname\":\"" + roomname + "\","
			x += 1
		print "\"id\":\"" + rmid + "\","
		print "\"roomowner\":\"" + roomowner + "\","
		print "\"participants\":\"" + participants + "\","
		print "\"latitude\":\"" + latitude + "\","
		print "\"longitude\":\"" + longitude + "\"}"
	print "]}"

#main program

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		displayRooms(db,cursor)
	except:
		cgi.print_exception()				