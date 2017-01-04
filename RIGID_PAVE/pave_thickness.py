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

traffic_level = ('extreme','very','heavy')
thick_min = (min_extr, min_very, min_heavy)
thick_max = (0, max_very, max_heavy)
 
for i in thick_max:
	if i == 0:
		query = 'insert into pave_thickness(traffic_level,thick_min,thick_max) values("%s",%d,%d)' %(traffic_level[thick_max.index(i)],thick_min[thick_max.index(i)], 0)
	else:
		query = 'insert into pave_thickness(traffic_level,thick_min,thick_max) values("%s",%d,%d)' %(traffic_level[thick_max.index(i)],thick_min[thick_max.index(i)], i)
	print(query)
	cur.execute(query)
	db.commit()


# Use all the SQL you like
cur.execute("SELECT * FROM pave_thickness")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()