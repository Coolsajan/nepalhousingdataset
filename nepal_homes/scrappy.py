import requests
from bs4 import BeautifulSoup
import pandas as pd

all_links=[]
full_det=[]


base_url='https://www.nepalhomes.com/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

for i in range(1,424):
    response=requests.get(f'https://www.nepalhomes.com/search?find_property_purpose=5db2bdb42485621618ecdae6&find_property_category=5d660cb27682d03f547a6c4a&page={i}&sort=1&find_selected_price_min=0&find_selected_price_max=5',headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')


    lists=soup.find_all('div',class_='property-listing-results-item')

    for list in lists:
            for links in list.find_all('a',href=True):
                if 'detail' in links['href']:
                    link=base_url+links['href']
                    if link not in  all_links:
                        all_links.append(link)
            


test='https://www.nepalhomes.com/detail/house-for-sale-NH24699'
count=0
for link  in all_links:
    response=requests.get(link,headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

    price=soup.find('p',class_='price m-0').text
    location=soup.find('p',class_='location').text
    features=soup.find('ul',class_='list-overview')
    locater=features.find_all('li')

    for i in range(len(locater)):
        if 'ROAD ACCESS' in locater[i].find('h3'):
            road_size=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'FACING' in locater[i].find('h3'):
            face=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'FLOOR' in locater[i].find('h3'):
            no_of_flat=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'PARKING' in locater[i].find('h3'):
            parking=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'BEDROOM' in locater[i].find('h3'):
            no_of_bedroom=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'BATHROOM' in locater[i].find('h3'):
            no_of_bathroom=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'FURNISH STATUS' in locater[i].find('h3'):
            furnishing=locater[i].find('h5').text
        else: pass

    for i in range(len(locater)):
        if 'LAND AREA' in locater[i].find('h3'):
            land_area=locater[i].find('h5').text
        else: pass



    housing_det={
        'price':price,
        'location':location,
        'land_size':land_area,
        'no_of_flat':no_of_flat,
        'no_of_bedroom':no_of_bedroom,
        'no_of_bathroom':no_of_bathroom,
        'furnishing':furnishing,
        'facing':face,
        'road_size':road_size

    }
    full_det.append(housing_det)
    count+=1
    print(count)


data_set_nepalhomes=pd.DataFrame(full_det)
data_set_nepalhomes.to_csv('raw_nepal_homes.csv',index=False)
