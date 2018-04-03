#!/usr/bin/python3

import sys
import sqlite3

# 01_read file
f = open(sys.argv[1],'r')
ori_txt = f.read()

# 02_seperate rows
rows = ori_txt.split('\n')

# 03_str to make table
column_H = rows[0]
string = [x+" text, "for x in column_H.split(',')]
string = ''.join(string)
sql_str = "CREATE TABLE sampledb (" + string[:-2] + ")"

# 04_connect db and make cursor
conn = sqlite3.connect('sample.db')
c = conn.cursor()

# 05_make flat table
try:
	c.execute(sql_str)
except sqlite3.OperationalError:
	c.execute('DROP TABLE sampledb')
	c.execute(sql_str)
finally:

# 06_insert data in table
	for string in rows[1:] :
		ins_str = ''
		for i in string.split(',') : 
			ins_str = ins_str + i + ','
		ins_str = "INSERT INTO sampledb VALUES (" + ins_str[:-1] + ")"
		c.execute(ins_str) 	

	conn.commit()
