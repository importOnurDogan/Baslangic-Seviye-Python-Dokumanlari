#SAYI TAHMİN  OYUNU

import random as r
rs=r.randint(1,100)
a = int(input("1 ile 100 arasında tutulan sayıyı, tahmin etmeye çalışın :\t"))
while(True):
    if (a<rs):
        a=int(input("daha yüksek sayı yazınız\n:\t"))
    elif (a>rs):
        a=int(input("daha küçük sayı yazınız\n:\t"))
    else:
        print("doğru tahmin.")
        break
    continue
