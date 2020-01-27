import requests as rq
from bs4 import BeautifulSoup

temp_data=[]
res = rq.get("https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films")                                                  
soup = BeautifulSoup(res.text, 'html.parser') 
table = soup.find("table",class_="wikitable plainrowheaders")
with open("marvel.txt","w+") as file:
    for items in table.find_all("tr"):
        data = [' '.join(item.text.split()) for item in items.find_all(['th','td'])]
        if len(data)>2:
             temp_data.append(data[0])


for items in temp_data[1:]:
    omid_api = rq.get("http://www.omdbapi.com/?i=tt3896198&apikey=7815f87e&t="+items)
    json = omid_api.json()
    try:
        print(items, json['imdbRating'])
    except:
        print(items,"has no rating")