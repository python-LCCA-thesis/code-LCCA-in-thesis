#!/usr/bin/python
import MySQLdb

#level_extr = ('extreme', min_extr)
#level_very = ('very', min_very, max_very)
#level_heavy = ('heavy', min_heavy, max_heavy)
#level_med = ('medium', min_med, max_med)
#level_light = ('light', min_light, max_light)

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

min_extr = 10**9
max_very = 10**9
min_very = 20*(10**6)
max_heavy = 20*(10**6)
min_heavy = 1*(10**6)
max_med = 1*(10**6) 
min_med = 3*(10**4)
max_light = 3*(10**4)
min_light = 0

level = ('extreme','very','heavy','medium','light')
min_i = (min_extr, min_very, min_heavy, min_med,min_light)
max_i = ('', max_very, max_heavy, max_med, max_light)
 
for i in max_i:
	if i == '':
		query = 'insert into traffic_level(level,min) values("%s",%d)' %(level[max_i.index(i)],min_i[max_i.index(i)])
	else:
		query = 'insert into traffic_level(level,min,max) values("%s",%d,%d)' %(level[max_i.index(i)],min_i[max_i.index(i)], i)
	print(query)
	cur.execute(query)
	db.commit()


# Use all the SQL you like
cur.execute("SELECT * FROM traffic_level")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row

db.close()