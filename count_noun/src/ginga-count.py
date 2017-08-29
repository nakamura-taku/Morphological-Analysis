# -*- coding: utf-8 -*-
import MeCab
import zipfile
import os.path
import urllib.request as req


hinshi = ["名詞"]
word_dic = {}

url = "http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
if not os.path.exists(local):
  print("ZIPファイルをダウンロード")
  req.urlretrieve(url, local)

zf = zipfile.ZipFile(local, 'r')
fp = zf.open('gingatetsudono_yoru.txt', 'r')
bindata = fp.read()
txt = bindata.decode('shift_jis')




def main():
  #f = open('example_text.txt', 'r')
  #txt = f.read()
  lines = txt.split("\r\n")
  for line in lines:
    # make a object for Morphological Analysis
    mecab = MeCab.Tagger("-Ochasen")
    mecab.parse('')
    node = mecab.parseToNode(line)
    while node:
      word = node.surface
      speech = node.feature.split(',')
      if speech[0] == hinshi[0]:
        if not word in word_dic:
          word_dic[word] = 0
        word_dic[word] += 1
      node = node.next

  keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
  for word,cnt in keys[:50]:
    print("{0}({1})\n".format(word,cnt), end="")


if __name__ == "__main__":
    main()
