#!/usr/bin/python3


## <title>   </title> 사이의 문자열을 출력

import sys
import re
from urllib.request import urlopen

#00_refresh로 다른 url로 연결(?)되는 경우엔 bytes->str 작업을 두 번 해야함!
def decode(url) : 
	URL = urlopen(url).read()
	try : 
		URL = URL.decode('utf-8')
	except : 
		URL = URL.decode('euc-kr')
	return URL

#01_http 확인 (urlopen은 www없는건 문제 없어도 http없으면 안됨)
p1 = re.compile('http')
url = sys.argv[1]
if not(bool(p1.match(url))) : 
	url = 'http://'+url


#03_정규표현식으로 <title> </title> 사이 내용을 찾기
URL = decode(url)
p2 = re.compile('<title>(.*)</title>')	#그룹핑
mObj = p2.search(URL)

if not (bool(mObj)) : 
	p3 = re.compile('url=(.*)"')
	m3 = p3.search(URL)
	URL = decode(m3.group(1))
	mObj = p2.search(URL)

print(mObj.group(1))
