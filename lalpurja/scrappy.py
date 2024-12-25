import requests

url = "https://backend.lalpurjanepal.com.np/properties/properties/"

querystring = {"search":"","area":"","ordering":"","is_owner_property":"null","purpose":"","property_type":"","category":"house","min_price":"","max_price":"","page":"50","collections":""}

payload = ""
headers = {"User-Agent": "insomnia/10.1.1"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)