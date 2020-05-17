# coding: utf-8

import MeCab
import re
from time import sleep

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

def word_counter(words):
    for word in words:
        if word in dict_word_count.keys():
            dict_word_count[word] += 1
        else:
            dict_word_count[word] = 1

# 除外単語リストの作成（最大閾値以上および最小閾値以下の出現頻度の単語）
def make_jogai(MAX,MIN):
    for k,v in sorted(dict_word_count.items(), key=lambda x:-x[1]):
        if v >= MAX or v <= MIN:
            #print(str(k) + ":" + str(v))
            jogai.append(k)

# Bug-Of-Wordsの適用（除外単語リストに含まれる単語の除外を各文書に対して行う）
def remove_jogai_from_document(document):
    for jogai_word in jogai:
        for word in document:
            if word == jogai_word:
                document.remove(jogai_word)
    return document

######## main funcion #################

a = open("document.txt", "r")
b = open("mecabed.txt", "w")

documents = []
dict_word_count = {}
jogai = []
MAX = 1000
MIN = 10

#単語-出現回数辞書を作成
for i in a:
    text = i.rstrip()
    output_words, output_text = Mplg(text)
    documents.append(output_words)
    word_counter(output_words)
a.close()

#2つの閾値を入力に除外単語リストを作成
make_jogai(MAX,MIN)

#各文書に対しBug-Of-Wordsを適用
for document in documents:
    jogai_document = remove_jogai_from_document(document)
    #print(jogai_document)
    text = ""
    for word in jogai_document:
        text = text + word + " "
    b.write(text +"\n")

b.close()

#words_set = set(hairetsu)
#print(words_set)
#dict_word = {}
#for n in words_set:
#    counter = 0
#    for word in hairetsu:
#        if word == n:
#            counter += 1
#            dict_word[n] = counter
#    print(n,counter)
#border = int(input("検索したい頻度の入力-->"))

#if counter >= border:
#    dict_word[n](n, counter)
