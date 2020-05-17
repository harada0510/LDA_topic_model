#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'

import gensim
from gensim import corpora, models, similarities
from time import sleep
import sys

#LDAの結果（各文書における各トピックへの確率分布）から所属トピックとその確率を選定．
def find_max(topics_per_document):
    list_A = []
    list_B = []
    for q in topics_per_document:
        list_A.append(q[0])
        list_B.append(q[1])
    max_prob  = max(list_B)
    max_index = list_B.index(max_prob)
    max_topic = list_A[max_index]
    print(GREEN+str(max_topic)+','+str(max_prob)+ENDC)
    print('___________________________')
    return max_topic,max_prob

# 辞書の作成
def make_dictionary(list3):
    print(GREEN+"辞書の作成を開始します。"+ENDC)
    dictionary = corpora.Dictionary(list3)
    #dictionary.filter_extremes(no_below=1, no_above=1) # 「頻度が１回のものは無視」というのを解除
    dictionary.save_as_text('dict_ittan.txt')
    dictionary = gensim.corpora.Dictionary.load_from_text('dict_ittan.txt')
    return dictionary

# 各トピックを構成するコーパス辞書の作成
def make_corpus(dictionary,list3):
    print(GREEN+"コーパスの作成を開始します。"+ENDC)
    corpus = [dictionary.doc2bow(text) for text in list3]
    corpora.MmCorpus.serialize('cop.mm', corpus)
    corpus = gensim.corpora.TextCorpus('cop.mm')
    return corpus

#ldaの適用
def maketopic_lda(dictionary,topic_N,id_list):
    corpus2 = corpora.MmCorpus('cop.mm')
    # num of topic
    #topic_N = 2
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus2, num_topics=topic_N, id2word=dictionary)
    lda.save("lda.model")
    for i in range(topic_N):
        print('TOPIC:', i, '__', lda.print_topic(i))
    index = 0
    for topics_per_document in lda[corpus2]:
        print(topics_per_document)
        page_id = id_list[index]
        max_topic,max_prob = find_max(topics_per_document)
        b.write(str(max_topic)+','+str(max_prob)+'\n')
        index += 1



#main部分
#N = int(input(GREEN+'How many topics do you want?\n-->'+ENDC))
N = int(sys.argv[1])

a = open('mecabed.txt','r')
b = open('lda_topic_'+str(N)+'.csv','w')
id_list = []
url_list = []
suggest_list = []
listB = []
cnt = 0
#各文書をリスト型に追加していく．
for i in a:
    content = i.rstrip()
    CNT     = content.split(' ')
    listB.append(CNT)
    id_list.append(str(cnt))
    cnt += 1
#辞書の作成
dictionary = make_dictionary(listB)
#コーパス辞書の作成
make_corpus(dictionary,listB)
#各文書をldaへ適用
maketopic_lda(dictionary,N,id_list)
a.close()
b.close() 
