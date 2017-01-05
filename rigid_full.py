#import RIGID_PAVE.generate_data
import RIGID_PAVE.module01
#import RIGID_PAVE.pave_thickness
import RIGID_PAVE.case01
import RIGID_PAVE.case02
import random
'''
number_axles = input('Enter number axles: ')
lst_number_axles = []
for i in range(number_axles):
	tmp = input('input weight '+str(i)+'th ...')
	lst_number_axles.append(tmp)
print(lst_number_axles)

print('Enter percent_number_axles: ')
lst_percent_axles = []
for i in range(number_axles):
	tmp = input('input percent '+str(i)+'th ...')
	lst_percent_axles.append(tmp)
print(lst_percent_axles)

ADTT = input('Enter number singles in first year: ')
print(ADTT)

n = input('Enter number singles in 3000 traffic: ')
print(n)

gr = input('Enter average annual growth rate of heavy vehicles: ')
print(gr)

t = input('Enter sevice time requirement design: ')
print(t)

n1s = RIGID_PAVE.module01.calculate_n1s(lst_number_axles,lst_percent_axles,ADTT,n)
print(n1s)

Ne = RIGID_PAVE.module01.ne(n1s,gr,t)
print(Ne)
'''

Ne = 250000000

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="7777777",    # your password
                     db="lcca")           # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

####################################################################

# Use all the SQL you like
cur.execute("SELECT * FROM traffic_level")
traffic_level = ''

for row in cur.fetchall():
    if Ne >= row[2]:
    	traffic_level = row[1]
    	print(traffic_level)
    	break

####################################################################

cur.execute("SELECT * FROM pave_thickness")
thick_min = 0
thick_max = 0

for row in cur.fetchall():
	if row[1] == traffic_level:
		thick_min = row[2]
		thick_max = row[3]
		print(thick_min,thick_max)

pave_thickness = round(random.uniform(thick_min,thick_max),2)
print(pave_thickness)

####################################################################

cur.execute("SELECT * FROM base_thickness")

datas_base = [('extreme',0.12,0.2,'poor concrete or roller compacted concrete'),('very',0.12,0.2,'poor concrete or roller compacted concrete'),('heavy',0.15,0.25,'crushed aggregate')]

base_material = ''
base_thick_min = 0
base_thick_max = 0

for row in cur.fetchall():
	if row[1] == traffic_level:
		base_material = row[4]
		base_thick_min = row[2]
		base_thick_max = row[3]
		print(base_material,base_thick_min,base_thick_max)

base_thickness = round(random.uniform(base_thick_min,base_thick_max),2)
print(base_material,base_thickness)

####################################################################

cur.execute("SELECT * FROM sub_thickness")

datas_sub = [('crushed aggregate type I',0.15,0.24),('crushed aggregate type II',0.15,0.24),('natural aggregate',0.15,0.30),('water bound macadam',0.15,0.18),('cinder, fly ash',0.15,0.18)]
sub_base = input('Enter subbase selected materinal: 1 - crushed aggregate type I; 2 - crushed aggregate type II; 3 - natural aggregate; 4 - water bound macadam; 5 - cinder, fly ash: ...')
if sub_base == 1:
	print('crushed aggregate type I')
	if sub_base == 2:
		print('crushed aggregate type II')
		if sub_base == 3:
			print('natural aggregate')
			if sub_base == 4:
				print('water bound macadam')
				if sub_base == 5:
					print('cinder, fly ash')

sub_thick_min = 0
sub_thick_max = 0

for data in datas_sub:
	for row in cur.fetchall():
		if row[1] == data[0]:
			sub_thick_min = row[2]
			sub_thick_max = row[3]
			print(sub_thick_min,sub_thick_max)
db.close()

sub_thickness = round(random.uniform(sub_thick_min,sub_thick_max),2)
print(sub_thickness)

####################################################################moi nhan gia tri 1

if base_material == 'poor concrete or roller compacted concrete':
#total thichkness
	hi1 = sub_thickness
	hi2 = base_thickness
	hi3 = pave_thickness
	hx = RIGID_PAVE.case01.total_thickness_layers(hi)
	print(hi)



'''
elif
'''
