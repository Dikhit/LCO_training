from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import bs4
executable_path = "C:\\Users\\Katlic\\Downloads\\web_drivers_chrome\\chromedriver.exe"


print("Please wait.. data proccessing....")
url = "https://courses.learncodeonline.in/learn"

driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)

courses = driver.find_elements_by_id('courseAvailList')

file = open("loc_courses.txt", "a+", encoding="utf-8")
for items in courses:
    file.write(items.text)
    file.write("\n\n")
    file.write("process end")

file.close()
driver.quit()

print("process complete")