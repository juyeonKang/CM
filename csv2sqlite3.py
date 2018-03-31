#!/usr/bin/python3

import re, sqlite3

flat = open('flat.csv').read()

p1 = re.compile('.*\s')
List = p1.findall(flat)

for i in range(len(List)):
	List[i] = List[i].replace("\n","")

'''
column = List[0].split(',')
for i in range(len(column)):
	if i<len(column)-1:
		column[i] = column[i]+" text, "
	else:
		column[i] = column[i]+" text"
column = ''.join(column)
'''

conn = sqlite3.connect('flat.db')
c = conn.cursor()

c.execute('CREATE TABLE flat (ISBN text, Title text, AuID text, AuName text, AuPhone text, PubID text, PubName text, PubPhone text, Price text)')
for item in List[1:len(List)] : 
	c.execute('INSERT INTO flat VALUES (?,?,?,?,?,?,?,?,?)', tuple(item.split(',')))

conn.commit()







#최소 매칭을 위해선 뒤에 ?를 붙여줄 것! (*? +? ?? {m,n}?)
