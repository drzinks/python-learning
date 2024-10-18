"""
API - Application Programming Interface
metody udostępnione publicznie, umożliwiace operowanie na zasobach
github public apis
"""
import requests
import json
from pprint import pprint
from webbrowser import open_new_tab
from datetime import datetime, timedelta

URL = "https://api.stackexchange.com/2.3/questions"
WEEK_BEFORE = timedelta(days = 7)
# order=desc&sort=activity&site=stackoverflow

params = {
    "order": "desc",
    "sort": "votes",
    "min": "10",
    "site": "stackoverflow",
    "fromDate": int((datetime.today() - WEEK_BEFORE).timestamp()),
    # "toDate" :"2019-08-28",
    # "tagged": "spark"
}


site = requests.get(URL, params)
if(site.status_code == 400):
    print("Not found")
    exit()
try:
    questions = site.json()
except json.decoder.JSONDecodeError:
    print("Wrong format")
else:
    i = 0
    for question in questions["items"]:
        link = question["link"]
        pprint(link)
        open_new_tab(link)
        i += 1
        if(i >= 3):
            break