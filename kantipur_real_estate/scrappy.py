import requests
from bs4 import BeautifulSoup
import pandas as pd

listings_links=[]
all_detials=[]

base_url='https://kantipurrealestate.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

listings_links=[]
url='https://kantipurrealestate.com/property'
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,'html.parser')
links=soup.find_all('a',href=True)

for link in links:
    if 'house' in link['href']:
        listings_links.append(base_url+link['href'])
    else: pass

#test='https://kantipurrealestate.com/property/house-sale-at-kathmandu-koteshwor-'

for links in listings_links:
    response=requests.get(links,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')
    price=soup.find('div',class_='property-price').text.strip()
    locater=soup.find_all('div',class_='col-md-3 other-details')
    land_area=locater[0].find_all('li')[0].text
    facing=locater[0].find_all('li')[1].text
    location=locater[1].find_all('li')[0].text
    road_size=locater[1].find_all('span')[2].text
    furnishing=locater[2].find_all('li')[0].text
    no_of_floors=locater[2].find_all('li')[2].text
    no_of_bedroom=locater[2].find_all('li')[3].text
    no_of_kitchen=locater[2].find_all('li')[4].text
    no_of_livingroom=locater[2].find_all('li')[5].text
    no_of_bathroom=locater[2].find_all('li')[6].text

    hosuing_det={
        'price':price,
        'location':location,
        'land_area':land_area,
        'no_of_flat':no_of_floors,
        'no_of_bedroom':no_of_bedroom,
        'no_of_bathroom':no_of_bathroom,
        'no_of_livingroom':no_of_livingroom,
        "no_of_kitchen":no_of_kitchen,
        "furnishing":furnishing,
        'facing':facing,
        'road_size':road_size
        }

    all_detials.append(hosuing_det)


dataset=pd.DataFrame(all_detials)
dataset.to_csv('kantipur_real_estate_raw.csv',index=False)
print(dataset)
