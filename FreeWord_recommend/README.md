
# FreeWord_recommend

- If you answer the question "What do you want to eat?", this script extracts noun and adjective from the answer.  
After that, the system go to a directory which have reviews of restaurants, and it counts the noun and the adjective in review of each restaurant.  
Finally, it introduces you restaurants in descending order.


# Description
## word_and_speech(txt)

- This function can morphological analysis of your sentence, and extracts noun and adjective from it as a list format.  
```
Example: 
You: ジューシーなお肉が食べたい
Rtn: ['ジューシー', '肉']
```

## main()

- main() goes to the "tabelog" directory which have many reviews of restaurants on tabelog.  
```
tabelog
-review_of_shopA.txt
-review_of_shopB.txt
-review_of_shopC.txt
...
```  
From each review, main() finds and counts numbers of the noun and the adjective you input.  
  
Finally, it introduces you restaurants in descending order of the number.
