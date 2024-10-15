import json

film = {
    "title": "Ale ja nie będę tego robił!",
    "release_year": 1969,
    "won_oscar": True,
    "actors": [
        "Arkadiusz Włodarczyk",
        "Wiolleta Włodarczyk"
    ],
    "budget": None,
    "credits": {
        "director": "Arkadiusz Włodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}

print(film["credits"])
print(json.dumps(film, ensure_ascii=False))  # dumps to String representation of json

with open("sample2.json", "w", encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False, indent=4, sort_keys=True)

import pprint

with open("sample2.json", encoding="UTF-8") as file:
    film2 = json.load(file)
    pprint.pprint(film2)
