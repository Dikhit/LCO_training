#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 22:31:48 2020
@author: sambhu7
"""
from selenium import webdriver
import bs4 

x=input('Input The range of  price ')
url='https://www.amazon.in/s?k=smartphone+under+RS'
url=url.replace('RS', x)
path='/Users/sambhu7/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
source=driver.page_source
soup=bs4.BeautifulSoup(source,'html.parser')

sp=soup.findAll('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
pr=soup.findAll('span',attrs={'class':'a-price-whole'})
#data=soup.findAll('div',attrs={'class':''})

l=len(sp)


for i in range(l):
    with open('/Users/sambhu7/spyder-py3/pro/lco/Day17/hw/am.txt','a+') as f:
        
        f.write(sp[i].get_text())
        f.write('\t')
        f.write(pr[i].get_text())
        f.write('\n')
    
# for i in range(l):
    
#     ls.append()

# for i in range(l):
#     ls.append(sp[i].get_text(),pr[i].get_text())
#     #print(pr[i].get_text())
#     prs=''
#     for j in (pr[i].get_text()):
#         if ord(j)>=48 and ord(j)<=57:
#             prs=prs+j
            
#     if int(prs)<=int(x):
#         ls.append(sp[i].get_text() +'\t'+ prs)
    
# for i in ls:
#     print(i)
#     print()
    
# with open('amazon.txt','w+') as f:
#     f.write(rq.get(url).text)