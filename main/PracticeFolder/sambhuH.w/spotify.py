#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 04:34:03 2020

@author: sambhu7
"""
from selenium import webdriver
import bs4

url='https://open.spotify.com/playlist/37i9dQZF1DWWQRwui0ExPn'
path='/Users/sambhu7/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get(url)
source=driver.page_source
soup=bs4.BeautifulSoup(source,'html.parser')
track=soup.select('div.tracklist-name.ellipsis-one-line') 
artist=soup.select('a.tracklist-row__artist-name-link')
l=len(track)
print(l)
#sp=soup.findAll('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})


for i in range(l):
    #print(track[i].get_text(),artist[i].get_text())
    with open('/Users/sambhu7/spyder-py3/pro/lco/Day17/hw/spotify.txt','a+') as f:
          f.write(str(i+1))
          f.write('.  ')
          f.write(track[i].get_text())
          f.write('\t')
          f.write(artist[i].get_text())
          f.write('\n')
          
          