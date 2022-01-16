#!/usr/bin/env python
import requests

url='http://www.baidu.com'
html=requests.get(url)
res=html.content.decode()
print(res)
