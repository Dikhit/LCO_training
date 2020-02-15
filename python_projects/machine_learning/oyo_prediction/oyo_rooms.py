from modules import *

driver = webdriver.Chrome(executable_path=executable_path)
driver.get("https://www.oyorooms.com/")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div/span[2]').click()

time.sleep(3)

list_of_hotel = []
address_of_hotel = []
ratings_of_hostel = []
offer_price_hotel = []
general_price_of_room = []

# Hotel Name
for index in range(1,40,2):
    xpath_hotel = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[1]/div[2]/div/a/h3'
    hotel_name = driver.find_element_by_xpath(xpath_hotel)
    hotel_name = hotel_name.text
    list_of_hotel.append(hotel_name)


time.sleep(3)

# Hotel Address
for index in range(1,40,2):
    try:
        xpath_address = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[1]/div[2]/div/div/span[1]'
        address = driver.find_element_by_xpath(xpath_address)
        address = address.text
        address_of_hotel.append(address)
    except:
        xpath_address = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[1]/div[2]/div[1]/div/span[1]'
        address = driver.find_element_by_xpath(xpath_address)
        address = address.text
        address_of_hotel.append(address)



# rating
for index in range(1,40,2):
    try:
        xpath_ratings = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[1]/div[3]/div/span[1]/span[1]'
        ratings = driver.find_element_by_xpath(xpath_ratings)
        ratings = ratings.text
        ratings = float(ratings)
        ratings_of_hostel.append(ratings)

    except:
        ratings_of_hostel.append('no rating')


# offer price
for index in range(1,40,2):
    try:
        xpath_offer_price = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/span[1]'
        offer_price = driver.find_element_by_xpath(xpath_offer_price)
        offer_price = offer_price.text
        offer_price = offer_price[1:]
        offer_price = int(offer_price)
        offer_price_hotel.append(offer_price)
    except:
        general_price_of_room.append('no rating')


# general price
for index in range(1,40,2):
    try:
        xpath_general_price = '//*[@id="root"]/div/div[3]/div/div/div[2]/section/div/div[2]/div[' + str(index) + ']/div/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/span[2]'
        general_price = driver.find_element_by_xpath(xpath_general_price)
        general_price = general_price.text
        general_price = general_price[1:]
        general_price = int(general_price)
        general_price_of_room.append(general_price)
    except:
        general_price_of_room.append('no rating')




print(type(ratings_of_hostel[0]))
if len(list_of_hotel) == len(address_of_hotel):
    df = pd.DataFrame({'oyo hotel' : list_of_hotel, 'address' : address_of_hotel, 'ratings' : ratings_of_hostel, 'offered price' : offer_price_hotel, 'original price' : general_price_of_room})
    df.to_csv('oyo_data.csv')


