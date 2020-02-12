from modules import *


driver = webdriver.Chrome(executable_path=executable_path)
driver.get("http://auxesis.in")
webdev = driver.find_elements_by_xpath('/html/body/footer/div[2]/div/div/div[4]/address/a')
for i in webdev:
    print(i.text)
time.sleep(2)
driver.quit()
