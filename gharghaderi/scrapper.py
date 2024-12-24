import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url='https://www.gharghaderi.com/'

listing_links=[]
all_det=[]
for i in range(51):
    url=f'https://www.gharghaderi.com/nepal-houses/page={i}'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')
    links_list=soup.find_all("div",class_='grid-thirds2 grid-thirds')
    for links in links_list:
        for link in links.find_all('a',href=True):
            listing_links.append(base_url+link['href'])


#test_url='https://www.gharghaderi.com/house/4335-House-On-Sale-Gharipatan-Pokhara/'

for linkss in listing_links:
    response=requests.get(linkss,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

    try:
        left_locater=soup.find_all('div',class_='left')[1]
        price=left_locater.find_all('td',class_='test')[0].text+(left_locater.find_all('td',class_='test1')[0].text.strip("रु. , ")).strip()
        land_area=left_locater.find_all('td',class_='test')[2].text+left_locater.find_all('td',class_='test1')[2].text.strip()
        no_of_floor=left_locater.find_all('td',class_='test')[3].text+left_locater.find_all('td',class_='test1')[3].text.strip()
        road_size=left_locater.find_all('td',class_='test')[4].text+left_locater.find_all('td',class_='test1')[4].text.strip()
    except: None
    try:
        right_locater=soup.find_all('div',class_='right')[1]
        facing=right_locater.find_all('td',class_='test')[0].text+right_locater.find_all('td',class_='test1')[0].text.strip()
        no_of_bedroom=right_locater.find_all('td',class_='test')[1].text+right_locater.find_all('td',class_='test1')[1].text.strip()
        no_of_bathroom=right_locater.find_all('td',class_='test')[2].text+right_locater.find_all('td',class_='test1')[2].text.strip()
        no_of_livingroom=right_locater.find_all('td',class_='test')[3].text+right_locater.find_all('td',class_='test1')[3].text.strip()
        no_of_kitchen=right_locater.find_all('td',class_='test')[4].text+right_locater.find_all('td',class_='test1')[4].text.strip()
        parking=right_locater.find_all('td',class_='test')[-2].text+right_locater.find_all('td',class_='test1')[-2].text.strip()
    except : None
    try:
        top_right_locater=soup.find_all('div',class_='right')[0]
        city_district=top_right_locater.find_all('td',class_='test1')[3].text.strip(),top_right_locater.find_all('td',class_='test1')[1].text.strip()
        location=",".join(city_district)
    except: None

    detials_housing={
        'price':price,
        'location':location,
        'land_area':land_area,
        'no_of_flat':no_of_floor,
        'no_of_bedroom':no_of_bedroom,
        'no_of_bathroom':no_of_bathroom,
        'no_of_livingroom':no_of_livingroom,
        "no_of_kitchen":no_of_kitchen,
        'no_of_parking':parking
        }


    all_det.append(detials_housing)



print(all_det)
print(listing_links)
df_ghargaderi=pd.DataFrame(all_det)
df_ghargaderi.to_csv('ghargaderi_raw.csv',index=False)

