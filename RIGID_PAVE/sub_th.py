#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

datas_sub = [('crushed aggregate type I',0.15,0.24),('crushed aggregate type II',0.15,0.24),('natural aggregate',0.15,0.30),('water bound macadam',0.15,0.18),('cinder, fly ash',0.15,0.18)]
for data in datas_sub:
	query = 'insert into sub_thickness(subgrade_material,thick_min,thick_max) values("%s",%f,%f)' %(data[0],data[1],data[2])
	print(query)
	cur.execute(query)
	db.commit()


# Use all the SQL you like
cur.execute("SELECT * FROM sub_thickness")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()