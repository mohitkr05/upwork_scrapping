import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

url = 

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
data = []

def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_data = []
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        table_data.append([ele for ele in cols if ele])
    return table_data


data.append(get_data(url))


anchor_tags = soup.findAll("a")
for anchor_tag in anchor_tags:
    if anchor_tag.text == "Last >>":
        last_page = anchor_tag['href'].split("=")[-1]
#
#for page in range(2,int(last_page)+1):
 #   updated_url = url + "&page=" + str(page)
  #  data.append(get_data(updated_url))

#print(data)
columns=['PostCode','Latitude','Longitude','Easting','Northing','Grid reference','Active']


df = pd.DataFrame(data)
df1 = df.T

print(tabulate(df1))
#print(df1.head)