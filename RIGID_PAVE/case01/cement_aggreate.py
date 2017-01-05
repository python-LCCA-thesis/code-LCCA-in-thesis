#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

cement_aggreate = ('silic','sandstone','gravel','granit','limstone')
ac = (12,12,11,10,7)
 
for i in cement_aggreate:
	query = 'insert into cement_aggreate(cement_aggreate,ac) values("%s",%d)' % (i, ac[cement_aggreate.index(i)])
	print(query)
	cur.execute(query)
	db.commit()


# Use all the SQL you like
cur.execute("SELECT * FROM cement_aggreate")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()