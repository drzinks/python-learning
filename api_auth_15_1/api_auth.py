import requests
import json
import webbrowser
from pprint import pprint

#x1uxtOdnPNVh7CCuSIpoYg35NIxUIUNB
params = {
    "api_key" : "x1uxtOdnPNVh7CCuSIpoYg35NIxUIUNB",
    "country" : "pl",
    "year": 2024
}

site = requests.get("https://calendarific.com/api/v2/holidays",params)
holidays = site.json()
pprint(holidays)