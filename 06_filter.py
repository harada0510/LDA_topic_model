# coding: utf-8

import sys

a = open("lda_topic_"+str(sys.argv[1])+".csv", "r")
b = open("pokemon.txt", "r")

lda = []
univ = []

for i in a:
    i = i.rstrip()
    lda.append(i)

for i in b:
    i = i.rstrip()
    univ.append(i)

a.close()
b.close()

c = open("lda_fix_"+str(sys.argv[1])+".csv", "w")

for i in range(0, len(univ)):
    #大学名とその大学文書のlda結果の紐付け
    c.write(univ[i] + ","+ lda[i] + "\n")

c.close()
