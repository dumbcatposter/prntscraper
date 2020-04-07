#!/usr/bin/env python
# encoding: utf-8

from lxml import html
import requests
import random
import shutil
from string import ascii_lowercase, digits

def random_url():
	url = ''.join(random.choice(digits + ascii_lowercase) for x in range(6))
	return url

if __name__ == "__main__":
    ids = []
	#Change the number in range() to specify the number of images you want to download
    for i in range(100):
        ids.append(random_url())
        page = requests.get("https://prnt.sc/" + ids[i], headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"})
        tree = html.fromstring(page.content)
        image = tree.xpath('//img[@id="screenshot-image"]/@src')
        print(image)
        if ("//st" not in image[0]):
            r = requests.get(image[0], stream=True)
            if r.status_code == 200:
                with open( "output/" + ids[i] + ".png", "wb") as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)