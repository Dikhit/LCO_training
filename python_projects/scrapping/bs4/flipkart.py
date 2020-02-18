import requests as rq
import bs4
user_input=int(input("Enter the maximum price of the products "))
data=rq.get("https://www.flipkart.com/search?q=mobiles")
data.status_code
soup=bs4.BeautifulSoup(data.text,"html.parser")
soup.title.get_text()
title=soup.findAll("div",attrs={"class":"_3wU53n"})
price=soup.findAll("div",attrs={"class":"_1vC4OE _2rQ-NK"})
for item in title:
    for i in price:
        i=str(i.get_text())
        i=''.join([j for j in i if j.isdigit()])
        i=int(i)
        if i<user_input:
            with open("new.txt", "a+") as file:
                file.write(item.get_text())
                file.write(str(i)) 
                file.write("\n")