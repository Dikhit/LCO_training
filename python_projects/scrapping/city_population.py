import bs4
import requests as rq
import datetime
import pprint

final_string = ""
counter = 0
r = rq.get("https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population")
bs=bs4.BeautifulSoup(r.text, "html.parser")
table_body=bs.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    if counter < 1:
        pass
    else:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        print(cols[1])
        break
        for i in range(len(cols)):
            res=(cols[0],cols[1],cols[2])
        each_details = " ".join(name for name in res)
        final_string = final_string + each_details + "\n\n"
    counter += 1

with open("city.txt", "w+") as file:
    file.write(final_string)