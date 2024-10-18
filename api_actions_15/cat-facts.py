import requests
import json
import webbrowser
from pprint import pprint

params = {
    "amount" : 5
}

URL = "https://cat-fact.herokuapp.com/facts/random"

facts = requests.get(URL, params).json()
for fact in facts:
    pprint(fact["text"])