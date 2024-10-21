import requests
import json
import webbrowser
from pprint import pprint

params = {
    "api_key" : "x1uxtOdnPNVh7CCuSIpoYg35NIxUIUNB",
    "country" : "pl",
    "year": 2024
}

site = requests.get("https://calendarific.com/api/v2/holidays",params)
holidays = site.json()["response"]["holidays"]
for holiday in holidays:
    if(holiday["type"][0] == 'National holiday'):
        pprint(holiday["date"]["iso"])
        pprint(holiday["name"])
