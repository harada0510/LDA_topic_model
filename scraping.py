# coding: utf-8

import wikipediaapi

def wiki(name):
    wiki_wiki = wikipediaapi.Wikipedia('ja')
    wiki = wiki_wiki.page(name)
#    print (wiki.exists())#wikipedia記事が存在するかいなか

#    print (wiki.title)#タイトル
#    print (wiki.summary)#要約
#    print (wiki.fullurl)#URL
#    print (wiki.text)#記事本体
    return wiki.text.replace('\n',' ')

a = open("university.txt", "r")
b = open("document.csv", "w")

for i in a:
    text = wiki(i.rstrip("\n"))
    b.write(text + "\n")

a.close()
b.close()
