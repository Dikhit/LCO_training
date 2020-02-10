from modules import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# session = rq.Session()

print("Just a sec..")

driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://www.youtube.com/playlist?list=WL")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

# driver = webdriver.Chrome(executable_path=executable_path)
# driver.get("https://www.youtube.com/playlist?list=WL", headers = headers)
time.sleep(3)

try :
    sign_in_button = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
    sign_in_button.click()
    time.sleep(3)
    email_address = driver.find_element_by_xpath('//*[@id="identifierId"]')
    email_address.send_keys("dikhitbhuyan@gmail.com")
    next_button = driver.find_element_by_class_name('CwaK9').click()
except:
    print("input field not found")
