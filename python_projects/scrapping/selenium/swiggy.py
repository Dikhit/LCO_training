from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import bs4
executable_path = "C:\\Users\\Katlic\\Downloads\\web_drivers_chrome\\chromedriver.exe"

driver=webdriver.Chrome(executable_path=executable_path)
driver.get('https://www.swiggy.com/')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="location"]').send_keys('JagatPura')

time.sleep(2)
address_clicker = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/span[2]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="open_filter"]/div/div/div[1]/div/div/a/div').click()
time.sleep(2)

num_of_res = driver.find_element_by_xpath('//*[@id="all_restaurants"]/div[2]/div[1]/div/div/div/div[2]')
number, res = num_of_res.text.split()
print(number)

resturant=driver.find_elements_by_class_name('nA6kb')
print(len(resturant))

driver.find_element_by_xpath('//*[@id="all_restaurants"]/div[2]/div[1]/div/div/div/div[3]/div[5]/span').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath('//*[@id="overlay-sidebar-root"]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/label[1]/div/div[1]').click()