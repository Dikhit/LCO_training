import requests as rq
from bs4 import BeautifulSoup
temp_data=""
res = rq.get("https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films")                                                  
soup = BeautifulSoup(res.text, 'html.parser') 
table = soup.find("table",class_="wikitable plainrowheaders")
with open("marvel.txt","w+") as file:
    for items in table.find_all("tr"):
        data = [' '.join(item.text.split()) for item in items.find_all(['th','td'])]
        if len(data)>2:
            temp_data=data[0]+"   "+data[1]+"\n"
            print(temp_data,"\n")
            file.write(temp_data)