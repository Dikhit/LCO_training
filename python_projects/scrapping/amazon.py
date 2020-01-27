import bs4
import requests as rq
import datetime
import pprint

price = int(input("Enter the price : "))
print("Please wait...")

amazon = rq.get("https://www.amazon.in/s?k=laptops")
html_content = amazon.text
final_amazon_text = ""
if amazon.status_code:
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    laptop_data = soup.find_all('span', attrs = {'class':'a-size-medium a-color-base a-text-normal'})
    laptop_price = soup.find_all('span', attrs = {'class' : 'a-offscreen'})
    for index in range(len(laptop_data)):
        i = str(laptop_price[index].text)
        i = ''.join([x for x in i if x.isdigit()])
        i = int(i)
        if i < price:
            final_amazon_text = final_amazon_text +  str(laptop_data[index].text) + "\t" + str(laptop_price[index].text) + "\n\n"
    with open("amazon.txt", "w+", encoding="utf-8") as file:
        file.write(final_amazon_text)
    print("Done")
else:
    print("status code is ", amazon.status_Code)