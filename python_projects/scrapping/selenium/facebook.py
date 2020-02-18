from modules import *


url = input("Enter the url : ")

driver = webdriver.Chrome(executable_path=executable_path)
driver.get(url)
if url == "https://www.facebook.com":
    email = input("Enter your email : ")
    print("Enter your password : ", end = " ")
    password = getpass.getpass()
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("u_0_b").click()
