#!/usr/bin/python3

import sqlite3

flat = open('flat.csv').read()

List = flat.split('\n')[:-1];
## 심지어 split('\n')으로 하면 굳이 \n을 지우지 않아도 됨! (2줄 절약)

column = [x+" text, " for x in List[0].split(',')]
column = ''.join(column)
sql = "CREATE TABLE flat (" + column[:-2] + ")"

conn = sqlite3.connect('flat.db')
c = conn.cursor()

c.execute(sql)  
for item in List[1:len(List)] : 
	c.execute('INSERT INTO flat VALUES (?,?,?,?,?,?,?,?,?)', tuple(item.split(',')))

conn.commit()







#최소 매칭을 위해선 뒤에 ?를 붙여줄 것! (*? +? ?? {m,n}?)
