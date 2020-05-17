#!/bin/sh

#python3 01_pokemon_wiki.py
echo "running mecab"
#python3 04_mecab.py
topic=(20 30 40 50 60 70 80)
for i in ${topic[@]}
do
echo "running lda"
python3 05_lda.py $i
echo "running combine"
python3 06_filter.py $i
nkf -Lw lda_fix_$i.csv > lda_fix_$i\_windows.txt
done
