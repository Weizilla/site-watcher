import requests
from bs4 import BeautifulSoup
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'} 
urls = ["https://primenow.amazon.com/gp/product/B01MUAGZ49", 
    "https://primenow.amazon.com/gp/product/B01LTHP2ZK"
]

with open("cookie.json") as c:
    cookies = json.load(c)

s = requests.Session()
for url in urls:
    page = s.get(url, headers=headers, cookies=cookies)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        oos = soup.find(string=re.compile("Currently Unavailable"))
        if oos:
            print("Too bad")
        else:
            print(soup.prettify())
