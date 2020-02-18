import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

temp_data=""
res = rq.get("https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films")                                                  
soup = BeautifulSoup(res.text, 'html.parser') 
table = soup.find("table",class_="wikitable plainrowheaders")

movies_name = []
release_date = []

with open("marvel.txt","w+") as file:
    for items in table.find_all("tr"):
        data = [' '.join(item.text.split()) for item in items.find_all(['th','td'])]
        if len(data)>2:
            temp_data=data[0]+"   "+data[1]+"\n"
            movies_name.append(data[0])
            release_date.append(data[1])
            file.write(temp_data)


df = pd.DataFrame({' movies ' : movies_name, ' realease date ' : release_date})
print(df)