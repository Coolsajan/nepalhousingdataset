import requests
from bs4 import BeautifulSoup
import pandas as pd

listing_links=[]
all_det=[]

base_url='https://gharsansarnepal.com'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}



for i in range(51):
    responce=requests.get(f'https://gharsansarnepal.com/category/home-for-sale-in-kathmandu/buy?page={i}',headers=headers)
    soup=BeautifulSoup(responce.content,'html.parser')

    links_list=soup.find_all('div','col-lg-4 col-md-6 col-sm-6 col-12')

    for links in links_list:
            for link in links.find_all('a',href=True):
                if 'house' in link['href']:
                    listing_links.append(link['href'])
    
count=0
test='https://gharsansarnepal.com/house-in-kathmandu/1185#'
for link in listing_links:
    responce=requests.get(link,headers=headers)
    soup=BeautifulSoup(responce.content,'html.parser')

    price=soup.find('div',class_='banner-sub-title').text.strip()
    location=soup.find('div',class_='overview-sub-title').text.strip()
    feature=soup.find_all('div',class_='contact-list')[1]
    flat_locater=soup.find('div',class_='overview-details')

    for i in range(len(feature.find_all('li'))):
        if 'Road Size' in feature.find_all('li')[i].text:
            road_size=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'land area' in feature.find_all('li')[i].text:
            land_area=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'beds' in feature.find_all('li')[i].text:
            no_of_bedroom=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'living' in feature.find_all('li')[i].text:
            no_of_livingroom=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'kitchen' in feature.find_all('li')[i].text:
            no_of_kitchen=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'bathrooms' in feature.find_all('li')[i].text:
            no_of_bathroom=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass
        
    for i in range(len(feature.find_all('li'))):
        if 'Property Face Direction' in feature.find_all('li')[i].text:
            facing=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    for i in range(len(feature.find_all('li'))):
        if 'Parking Space' in feature.find_all('li')[i].text:
            parking=feature.find_all('li')[i].text.split(':')[1].strip()
        else: pass

    try:
        no_of_flat=flat_locater.find_all('p')[1].text
    except:
        no_of_flat=None


    housing_det={
            'price':price,
            'location':location,
            'land_size':land_area,
            'no_of_flat':no_of_flat,
            'no_of_bedroom':no_of_bedroom,
            'no_of_bathroom':no_of_bathroom,
            'no_of_living':no_of_livingroom,
            'no_of_kitchen':no_of_kitchen,
            'facing':facing,
            'road_size':road_size


        } 
    all_det.append(housing_det)
    count+=1
    print(count)

data_set=pd.DataFrame(all_det)
data_set.to_csv('gharsansar_raw1.csv',index=False)



