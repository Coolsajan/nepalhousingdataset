import requests
import pandas as pd

alldet=[]
alldata=[]
for i in range(1,287):
    import requests

    url = "https://api.basobaas.com/api/collections/properties/records"

    querystring = {"page":f"{i}","perPage":"1","filter":"(active = true && deleted = false && (category.name = 'House') && approved = true && status = 'Sale' && expired = false && approved = true)","expand":"category, property_features(house), property_features(property).feature, user, user.agency, area.city","sort":"-updated"}

    payload = ""
    headers = {"User-Agent": "insomnia/10.1.1"}

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    data=response.json()
    alldata.append(data)



for data in alldata:

    try:
        location=data['items'][0]['address']
    except:
        location=None
    try:
        facing=data['items'][0]['detail']['property_face']
    except:
        facing=None
    try:    
        land_area=data['items'][0]['detail']['land_area']
    except:
        land_area=None
    try:    
        road_acess=data['items'][0]['detail']['road_access_in_feet']
    except:
        road_acess=None
    try:    
        furniture=data['items'][0]['detail']['furnishing']
    except:
        furniture=None
    try:
        bedroom=data['items'][0]['detail']['bedroom_count']
    except:
        bedroom=None
    try:    
        bathroom=data['items'][0]['detail']['bathroom_count']
    except:
        bathroom=None
    try:    
        livingroom=data['items'][0]['detail']['livingroom_count']
    except:
        livingroom=None
    try:    
        kitchen=data['items'][0]['detail']['kitchen_count']
    except:
        kitchen=None
    try:
        parking=data['items'][0]['detail']['parking_space_count']
    except:
        parking=None
    try:    
        floors=kitchen=data['items'][0]['detail']['floors']
    except:
        floors=None
    try:
        price=data['items'][0]['price']
    except:
        price=None


    det={
        'price':price,
        'location':location,
        'area':land_area,
        'facing':facing,
        "no_of_bedroom":bedroom,
        'no_of_bathroom':bathroom,
        'no_of_livingroom':livingroom,
        'no_of_kitchen':kitchen,
        'parking':parking,
        'road_size':road_acess,
        'furniture':furniture,
        'floors':floors
    }

    alldet.append(det)

import pandas as pd
dataset=pd.DataFrame(alldet)
dataset.to_csv('basobas.csv',index=False)