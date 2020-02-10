from selenium import webdriver
from selenium.webdriver.common.keys import Keys
executable_path = "C:\\Users\\Katlic\\Downloads\\web_drivers_chrome\\chromedriver.exe"


driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://www.veenaworld.com/india/jaipur-tour-packages/ct")
tours = []
for i in range(2,10):
    xpath = '//*[@id="searchList"]/div/div[1]/div/div[1]/div[' + str(i) + ']/vw-tile-item-v3/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/a/h3'
    try:
        tour = driver.find_element_by_xpath(xpath)
        tours.append(tour)
    except:
        print("not found")
        
prices = []
for i in range(2,10):
    xpath = '//*[@id="searchList"]/div/div[1]/div/div[1]/div[' + str(i) + ']/vw-tile-item-v3/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/a'
    try:
        price = driver.find_element_by_xpath(xpath)
        prices.append(price)
    except:
        print("not found")
        
for i in range(8):
    print(tours[i].text)
    print(prices[i].text)
    print('\n\n')