#!/usr/bin/python3

## <title>   </title> 사이의 문자열을 출력

import sys
import re
from urllib.request import urlopen


#01_http 확인 (urlopen은 www없는건 문제 없어도 http없으면 안됨)
p1 = re.compile('http')
url = sys.argv[1]
if not(bool(p1.match(url))) : 
	url = 'http://'+url

#02_정규표현식을 사용(?)하기 위해선 bytes->str로 decode(예외처리 이용)
URL = urlopen(url).read()
try : 
	URL = URL.decode('utf-8')
except : 
	URL = URL.decode('euc-kr')

#03_정규표현식으로 <title> </title> 사이 내용을 찾기
p2 = re.compile('<title>(.*)</title>')	#그룹핑
mObj = p2.search(URL)

print(mObj.group(1))
