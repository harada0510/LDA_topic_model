# coding: utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E5%A4%A7%E5%AD%A6%E4%B8%80%E8%A6%A7")

soup = BeautifulSoup(r.text, "html.parser")


b=open("url.csv","w")
flg = 0
for a in soup.find_all("a"):

    if "愛国学園大学" == a.text:
        flg = 1

    if flg == 1 and "大学" in a.text:
        print(a.text, a.attrs['href'])
        b.write(a.text + "\n")

    if "和洋女子大学" == a.text:
        flg = 0

b.close()
