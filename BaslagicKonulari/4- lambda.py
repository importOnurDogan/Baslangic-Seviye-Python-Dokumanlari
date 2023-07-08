"İsimlendirme yapmadan fonksiyon tanımlama"

def old_sum(a,b):
    return a+b
print(old_sum(4,5))


new_sum = lambda a,b: a+b
print(new_sum(8,9))


sirasiz_liste = [("b",3),("a",8),("d",12),("c",1)]
print(sorted(sirasiz_liste, key= lambda  x:x[1]))


"örnek"
liste =[1,2,3,4,5]
for i in liste:
   print(i+10)
"Lambda yani isimsiz fonksiyon yapısıyla birlikte kullanılabilen ve bize vektörel işlemler" \
"yapmamızı sağlar."


"Map"
print(list(map(lambda x: x*10, liste)))
"Filter"
liste=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2 == 0 , liste)))
"Reduce"
from functools import reduce
liste =[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda a,b: a+b, liste))