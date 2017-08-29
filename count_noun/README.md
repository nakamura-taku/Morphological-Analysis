
# Count noun

- You can know what word is the most appering in the text.  
And the number.

## You need...
- "count.py" is a script.  
"example_text.txt" : the text you want to count noun.  
```
python count.py
```

- "ginga-count.py" is a example script with "銀河鉄道の夜", which is a famous Japanese novel.
The right is free.  
You have to download the text from AOZORA BUNKO.  
How to do it...  
```
url = "http://www.aozora.gr.jp/cards/000081/files/456_ruby_145.zip"
local = "456_ruby_145.zip"
if not os.path.exists(local):
  print("ZIPファイルをダウンロード")
  req.urlretrieve(url, local)

zf = zipfile.ZipFile(local, 'r')
fp = zf.open('gingatetsudono_yoru.txt', 'r')
bindata = fp.read()
txt = bindata.decode('shift_jis')
```
