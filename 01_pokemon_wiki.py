# coding: utf-8

PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'

import requests
import json
from bs4 import BeautifulSoup
from time import sleep
from extractcontent3 import ExtractContent

##### ExtractContent （本文のみ抽出）########

def extractor(html):
    extractor = ExtractContent()
    opt = {"threshold":50}
    extractor.analyse(html)
    text, title = extractor.as_text()
    html, title = extractor.as_html()
    title = extractor.extract_title(html) 
    return text.replace("\n","")

####main#########

r = requests.get("https://wiki.xn--rckteqa2e.com/wiki/%E3%83%9D%E3%82%B1%E3%83%A2%E3%83%B3%E4%B8%80%E8%A6%A7")

soup = BeautifulSoup(r.text , "html.parser")
b = open("pokemon.txt", "w")
c = open("document.txt", "w")

flag = 0
num = 0

#ポケモン-出現回数の辞書型
dict_pokemon_num = {}

#ポケモン-ポケモンのページへの相対リンク
dict_pokemon_url= {}

# フシギダネからザルードまでのaタグを抽出して辞書に追加してく
for a in soup.find_all("a"):
    if 'フシギダネ' == a.text:
        flag = 1
    if flag == 1 and a.text not in dict_pokemon_num.keys() and a.attrs["title"] != "フォルム":
        dict_pokemon_num[a.text] = 1
        dict_pokemon_url[a.text] = a.attrs["href"]
        #print(a.text)

    elif flag == 1 and a.text in dict_pokemon_num.keys():
        #print(a.text)
        dict_pokemon_num[a.text] += 1
    if "ザルード" == a.text:
        flag = 0
num = 1

for k,v in dict_pokemon_num.items():
    if v< 2:
        r = requests.get("https://wiki.xn--rckteqa2e.com"+dict_pokemon_url[k])
        r.encoding = r.apparent_encoding
        html = r.text
        text = extractor(html)
        if text != "":
            b.write(k+"\n")
            c.write(text+ "\n")
        print(CYAN, str(num),GREEN,k,BLUE,"https://wiki.xn--rckteqa2e.com"+dict_pokemon_url[k],ENDC,text)
        num += 1
        sleep(0.5)

c.close()
b.close()
