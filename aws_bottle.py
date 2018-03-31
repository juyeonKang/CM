#!/usr/bin/python3
import sqlite3
from bottle import route, run, template

@route('/')
def main():
	return '<b> Hello:D<br> this page is my first page! </b>'

@route('/db')
def db():
	conn = sqlite3.connect('flat.db')
	c = conn.cursor()
	c.execute("SELECT * FROM flat")
	result=c.fetchall()
	c.close()
	output = template('make_table', rows=result)
	return str(output)

run(reloader = True, host='0.0.0.0', port=8080)

