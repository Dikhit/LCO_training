#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 01:22:44 2020
@author: sambhu7
"""
from selenium import webdriver
import requests as rq
import bs4 

url='https://www.pexels.com/search/coding/'

path='/Users/sambhu7/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
source=driver.page_source
soup=bs4.BeautifulSoup(source,'html.parser')

img=soup.select('img.photo-item__img')
l=[]
#jpg=soup.select('src')
#print(img)

for i in img:
    l.append(i.get('srcset'))
    
#print(l)
    
c=1
    
for i in l:
    ind=i.index(',')
    s_=i[ind+2::]
    print(s_)
    r=rq.get(s_)    
    s__=r.content
    with open('/Users/sambhu7/spyder-py3/pro/lco/Day17/hw/sg/image'+str(c)+'.jpeg','wb+') as f:
          f.write(s__)
    c+=1

    
# import requests
# >>> response = requests.head('http://example.com')
# >>> response.headers
#     {'connection': 'close',
#  'content-encoding': 'gzip',
#  'content-length': '606',
#  'content-type': 'text/html; charset=UTF-8',
#  'date': 'Fri, 11 Jan 2013 02:32:34 GMT',
#  'last-modified': 'Fri, 04 Jan 2013 01:17:22 GMT',
#  'server': 'Apache/2.2.3 (CentOS)',
#  'vary': 'Accept-Encoding'}    