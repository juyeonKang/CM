import re

p = re.compile('(\d{3})-\d{}-(\d{4})')
test = 'today : 2018-02-25 , 010-2927-9686:JY, 111-1111-1111'
m=p.findall(test)
print(test)
print(m)
