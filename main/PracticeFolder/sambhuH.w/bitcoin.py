#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 05:11:24 2020

@author: sambhu7
"""


from selenium import webdriver
from datetime import datetime
import time
import bs4 



url='https://markets.bitcoin.com/'
path='/Users/sambhu7/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
time.sleep(2)
for i in range(30):
    source=driver.page_source
    soup=bs4.BeautifulSoup(source,'html.parser')
    bt=soup.select('div.sc-1a7ju4v-5.kYZUrO')
    data=bt[0].get_text()
    now = datetime. now()
    
    with open('/Users/sambhu7/spyder-py3/pro/lco/Day17/hw/bitcoin.txt','a+') as f:
              f.write(str(now))
              f.write('\t')
              f.write(data)
              f.write('\n')
              
    time.sleep(30)
    