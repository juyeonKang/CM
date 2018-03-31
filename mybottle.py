import sqlite3
from bottle import route, run, request



@route('/')
def main():
	return '<b> It Works! </b>'

@route('/input')
def myinput():
	num1 = request.GET.num1
	num2 = request.GET.num2
	result = int(num1)+int(num2)
	return str(result)

run(host='0.0.0.0', port=8080)
