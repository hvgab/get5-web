from pprint import pprint

import requests
from bs4 import BeautifulSoup

url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2870304806"

r = requests.get(url)

pprint(r.text)

soup = BeautifulSoup(r.text)
image = soup.find("meta", property="og:image")
image_url = image["content"]

print()
print()
print(image)
print(image_url)
print()
print()

# with open('steam.html', 'w') as output:
#    output.write(r.text)
