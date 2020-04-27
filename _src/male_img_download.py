# import urllib.request

# urllib.request.urlretrieve("http://www.gunnerkrigg.com//comics/00000001.jpg", "00000001.jpg")

import os
import requests

# for filename in os.listdir(f"{os.path.dirname(__file__)}/../assets/items_female"):

x = requests.get("https://w3schools.com/python/demopage.htm")

print(x.text)
