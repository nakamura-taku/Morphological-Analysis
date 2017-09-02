import MeCab
import glob
import os


hinshi = ["名詞", "形容詞"]
#hinshi = ["名詞"]


def word_and_speech(txt):
  """
  Get word and speech list
  """

  mecab = MeCab.Tagger('-Ochasen')
  mecab.parse('')
  node = mecab.parseToNode(txt)

  word_li = []
  while node:
    word = node.surface
    speech = node.feature.split(',')
    for i in range(len(hinshi)):
      if speech[0] == hinshi[i]:
        word_li.append(word)
    node = node.next

  return word_li



def main():
  list = glob.glob("./tabelog/*.txt")

  print("What do you want to eat?")
  order = input(">>>  ")
  result = word_and_speech(order)
  print("Your order is {}.\n".format(result))

  shop_ns_dic = {}
  for li in list:
    f = open(li, "r")
    txt = f.read()
    count = 0
    for i in range(len(result)):
      if txt.find(result[i]) >= 0:
        name, ext = os.path.splitext(os.path.basename(li))
        if not str(name) in shop_ns_dic:
          shop_ns_dic[name] = 0
        shop_ns_dic[name] += txt.count(result[i])

  keys = sorted(shop_ns_dic.items(), key=lambda x:x[1], reverse=True)

  print("I found {} shops".format(len(keys)))
  print("I recommend you...")
  cnt = 0
  while(cnt < len(keys)):
    print("How about this shop?")
    print(keys[cnt][0])
    print("Good or Bad?\n")
    feedback = input(">>>  ")
    if feedback == "Good":
      print("Thank you")
      break
    elif feedback == "Bad":
      print("I'm sorry...")
      cnt += 1
      continue
    else:
      print("Please, input 'Good' or 'Bad'")
      continue



if __name__ == "__main__":
  main()
