#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

datas = [('extreme',0.12,0.2,'poor concrete or roller compacted concrete'),('very',0.12,0.2,'poor concrete or roller compacted concrete'),('heavy',0.15,0.25,'crushed aggregate')]
for data in datas:
	query = 'insert into base_thickness(traffic_level,thick_min,thick_max,material) values("%s",%f,%f,"%s")' %(data[0],data[1],data[2],data[3])
	print(query)
	cur.execute(query)
	db.commit()

# Use all the SQL you like
cur.execute("SELECT * FROM base_thickness")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()