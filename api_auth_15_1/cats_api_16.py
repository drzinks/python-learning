import json
from pprint import pprint
import requests
import credentials

SUB_ID = "drzinks"
HTTP_SUCCESS = 200

def get_favs_by_id(sub_id):
    URL = "https://api.thecatapi.com/v1/favourites"
    parameters = {
        "attach_image" : 1,
        "limit" : 10,
        "sub_id" : sub_id
    }
    return requests.get(URL,parameters, headers = credentials.headers).json()

def get_random_cat():
    URL = "https://api.thecatapi.com/v1/images/search"
    return requests.get(URL, headers = credentials.headers).json()

def add_new_fav_cat(sub_id, cat_id):
    URL = "https://api.thecatapi.com/v1/favourites"
    cat_data = {
        "sub_id": sub_id,
        "image_id": cat_id
    }
    response = requests.post(URL, json = cat_data, headers=credentials.headers)
    return response

def del_fav_cat(cat_id, fav_cats):
    URL = "https://api.thecatapi.com/v1/favourites/"+cat_id
    response = requests.delete(URL,headers=credentials.headers)
    if(response.status_code != HTTP_SUCCESS):
        print("Such cat doesn't exist in db.")
    else:
        fav_cats
    # return response


print("\nHere are your favourite cats: ")
fav_cats = get_favs_by_id(SUB_ID)
while(True):
    pprint(fav_cats)
    print("\nHere is a random cat")
    random_cat = get_random_cat()
    print(random_cat[0]["url"])
    decision = input("""
    want to add it? (y/n) 
    or 
    maybe delete (d) a cat
    or 
    exit(e)
    """)
    if(decision =="y"):
        add_new_fav_cat(SUB_ID,random_cat[0]["id"])
        # pprint(get_favs_by_id(SUB_ID))
    elif(decision == 'n'):
        print("It's a pitty.")
    elif(decision == "d"):
        print("Here are ids: ")
        for cat in fav_cats:
            print(cat["id"])
        cat_id = input("Enter the id of cat to be removed: ")
        del_fav_cat(cat_id,fav_cats)
    elif(decision == "e"):
        break
    else:
        print("no working key chosen.")
