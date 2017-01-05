#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

min_extr = 0.32
max_very = 0.32
min_very = 0.28
max_heavy = 0.28
min_heavy = 0.25
'''
traffic_level = ('extreme','very','heavy')
thick_min = (min_extr, min_very, min_heavy)
thick_max = (1, max_very, max_heavy)
'''
datas = [('extreme',0.32,1.0),('very',0.28,0.32),('heavy',0.25,0.28)]
for data in datas:
	query = 'insert into pave_thickness(traffic_level,thick_min,thick_max) values("%s",%f,%f)' %(data[0],data[1],data[2])
	print(query)
	cur.execute(query)
	db.commit()


# Use all the SQL you like
cur.execute("SELECT * FROM pave_thickness")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()