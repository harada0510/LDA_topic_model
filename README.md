# LDA_topic_model


# 目的
文書集合を作成し，作成された文書集合に対しLDAトピックモデルを適用することで，ポケモンのクラスタリングを行う．

# 大まかな流れ
- Webスクレイピングで文書を収集する
- 欠損処理を加える
-　mecabによる形態素解析
- 文書集合の分かち書き
- Bug-Of-Wordsの適用
- LDAトピックモデルを適用
- ポケモンとLDA結果の紐付け
- nkfコマンドでwindows用改行文字に直したファイル出力

# 実行方法
ポケモンのクラスタリング

```
# get pokemon name and document
$ python3 01_pokemon_wiki.py
# check same lines
$ wc -l pokemon.txt
$ wc -l document.txt
# mecab
$ python3 04_mecab.py
# apply to lda with 50 topic (you can change like 20, 40, 100 ...)
$ python3 05_lda.py 50
# linking pokemon name with lda result
$ python3 06_filter.py
```
