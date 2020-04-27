import urllib.request
import os
import requests
import json
import numpy as np

done_ids = []
for filename in os.listdir(f"{os.path.dirname(__file__)}/../assets/items_male"):
    if filename.endswith(".jpg"):
        done_ids.append(filename[:-4])


x = requests.get("https://cdn.aq3d.cc/store/items.txt")

# 470 px imgs height


lists = [
    (str(json.loads(row)["id"]), json.loads(row)["url_m"])
    for row in x.text.split(",\n")[:-1]
    if json.loads(row)["url_m"] != "" and not str(json.loads(row)["id"]) in done_ids
]

list_png = [i for i in lists if i[1].endswith(".png") or i[1].endswith(".PNG")]
list_jpg = [i for i in lists if i[1].endswith(".jpg") or i[1].endswith(".JPG")]

[os.system(f"wget -O {os.path.dirname(__file__)}/../assets/items_male/{liste[0]}.png {liste[1]}") for liste in list_png]
[os.system(f"wget -O {os.path.dirname(__file__)}/../assets/items_male/{liste[0]}.jpg {liste[1]}") for liste in list_jpg]


# print(lists)
