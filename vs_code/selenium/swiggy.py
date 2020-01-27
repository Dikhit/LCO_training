from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

import bs4
executable_path = "C:\\Users\\Katlic\\Downloads\\web_drivers_chrome\\chromedriver.exe"

driver = webdriver.Chrome(executable_path = executable_path)
driver.maximize_window()

driver.get("https://www.swiggy.com/")
location = driver.find_element_by_xpath("//*[@id='root']/div[1]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[2]")
location.click()

try:
    driver.implicitly_wait(20)
    search_bar = driver.find_element_by_xpath("//*[@id='root']/div[1]/header/div/div/div/span[2]")
    search_bar.click()
    print("Search Bar Element clicked...")
    input_address_element = driver.find_element_by_xpath("//*[@id='overlay-sidebar-root']/div/div/div[2]/div/div/div[2]/div[2]/div/input")
    input_address_element.send_keys("Jagatpura flyover")
    input_address_element.send_keys(Keys.ENTER)
    time.sleep(5)
    
    select_place = driver.find_elements_by_class_name("Ku2oK")
    for i in range(len(select_place)):
        select_place[0].click()
    
    driver.send_keys(keys.RETURN)
    print(driver.current_url)
    
    
except:
    print("not found")