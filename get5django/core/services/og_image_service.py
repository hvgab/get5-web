
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from service_objects.services import Service
from django import forms

class OgImageService(Service):
    url = forms.URLField()

    def process(self):
        url = self.cleaned_data['url']

        # url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2870304806'

        # Get Request
        r = requests.get(url)

        soup = BeautifulSoup(r.text)
        image = soup.find("meta", property="og:image")
        
        try:
            return image['content']
        except Exception as e:
            return None
