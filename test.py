from urllib.request import urlopen
import sys

url=sys.argv[1]
f=urlopen(url)
b=f.read()
B=b.decode('utf-8')


n1=B.find('<title>')
n2=B.find('</title>')

print(B[n1+7:n2])
