# coding: utf-8

GREEN = "\033[92m"
ENDC = "\033[0m"

import requests
from extractcontent3 import ExtractContent	
import MeCab
import re
from time import sleep

def extractor(html):
    extractor = ExtractContent()
    opt = {"threshold":50}
    extractor.analyse(html)
    text, title = extractor.as_text() 
    return text

def Mplg(text):
    output_words = []
    output_text  = ''
    m = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/ipadic')
    soup = m.parse (text)
    for row in soup.split("\n"):
        word =row.split("\t")[0]
        if word == "EOS":
            break
        else:
            pos = row.split("\t")[1]
            slice = pos.split(",")
            if len(word) > 1:
                if slice[0] == "名詞":
                    output_words.append(word)
                    output_text = output_text + ' ' + word
                elif slice[0] in [ "形容詞"]:
                    if slice[5] == "基本形":
                        output_words.append(slice[-3])#活用していない原型を取得(JSON型)
                        output_text = output_text + ' ' + slice[-3]
    return output_words, output_text

def main(url):
    r = requests.get(url)
    r.raise_for_status()
    html = r.text
    text = extractor(html)
    text = text.replace(',',' ').replace('\n',' ').replace('\t','').replace('\r','')
    text = re.sub(r'&#91;([0-9]+)&#93;', ' ', text)
    #print(text)

    hairetsu, mecabed_text = Mplg(text)
    #print(hairetsu)
    
    return hairetsu

#url = "https://ja.wikipedia.org/wiki/%E6%A5%BD%E5%A4%A9"
#mecab = main(url)
#print(mecab)

text = " "
a = open("url.csv", "r")
b = open("result.csv", "w")


for i in a:
    sleep(2)
    row = i.rstrip().split(",")
    url = row[1]
    name = row[0]

    #url = i.rstrip().split(",")[1]
    #name = i.rstrip().split(",")[0]
    print(GREEN + name + ENDC, url)

    mecab = main(url)
    #print(mecab)
    for index in mecab:
        text = text + index + " "
    b.write(text+"\n")
a.close()
b.close()

#words_set = set(hairetsu)
#print(words_set)
#dict_word = {}
#for word in words_set:
#    counter = 0
#    for w in hairetsu:
#        if word == w:
#            counter += 1
#            dict_word[word] = counter
            #print(word,w,str(counter))

#print (dict_word)
#dict_word = sorted(dict_word.items(), key=lambda x:x[1], reverse=True)
#dict_word = dict(dict_word)
#print(dict_word)

#for key, value in dict_word.items():
#    print(key, str(value))

#閾値からの単語の出力
#border = int(input("検索したい頻度の入力-->"))
#for key ,value in dict_word.items():
#    if border <= value:
#        print(key, str(value))

#key = input("検索したい単語を入力してください-->")
#flag = key in dict_word.keys()
#if flag == True:
#    print(key+"の頻度は"+str(dict_word[key]))
#else:
#    print("その検索語は存在しません")

#flag = key in dict_word.keys()

#try:
#    print(key+"の頻度は"+str(dict_word[key]))
#except ValueError:
#    print("その検索語は存在しません")