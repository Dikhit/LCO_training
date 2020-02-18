from modules import *

def main():
    url = input("What you want to search : ")
    url = url + "wikipedia"
    driver = webdriver.Chrome(executable_path=executable_path)
    driver.get("https://www.google.com")

    search_bar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(url)
    search_bar.send_keys(Keys.ENTER)

    value = driver.find_element_by_class_name('LC20lb').click()

    # for items in value:
    #     print(items.text)

    driver.maximize_window()

    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    x = 1
    while True:
        pyautogui.screenshot("C:\\Users\\Katlic\\Pictures\\auto_screen_shots\\images" + str(x) + ".png")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        x += 1
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(100)

if __name__ == "__main__":
    main()