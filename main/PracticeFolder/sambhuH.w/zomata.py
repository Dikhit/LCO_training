#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 02:25:18 2020

@author: sambhu7
"""


#Use selenium to scrape Zomato website for resturant data.
from selenium import webdriver
import bs4



#url = "https://www.zomato.com/city/town-restaurants"
url='https://www.zomato.com/jaipur/malviya-nagar-restaurants'
path='/Users/sambhu7/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=path)
city = input("Enter the city : ").lower()
near_by = input("Enter the nearest town : ").lower()
near = near_by.split(" ")
near1 = "-".join(near)
mod = url.replace("city",city)
new_url= mod.replace("town",near1)


driver.get(url)
source=driver.page_source

soup=bs4.BeautifulSoup(source,'html.parser')
name=soup.select('a.result-title.hover_feedback.zred.bold.ln24.fontsize0')
data=soup.select('div.search-page-text.clearfix.row')

l=len(name)

for i in range(l):
    print(name[i].get_text())
    print(data[i].get_text().split())
    print('\n\n')



