# coding: utf-8

a = open("mecabed.txt", "r")
b = open("mecabed_fixed.txt", "w")

words_set = set(hairetsu)
print(words_set)
dict_word = {}
for word in words_set:
    counter = 0
    for w in hairetsu:
        if word == w:
            counter += 1
            dict_word[word] = counter
             #print(word,w,str(counter))
 
print (dict_word)
dict_word = sorted(dict_word.items(), key=lambda x:x[1], reverse=True)
dict_word = dict(dict_word)
print(dict_word)

a.close()
b.close()
