import math
print(math.factorial(5))


from math import*
print(factorial(5))
#from math import* -math- modülündeki bütün fonksyonları alır.


from math import floor,ceil
print(ceil(5))
print(floor(8.9))
#from math import floor,ceil -math- modülündeki istediğimiz fonksyonlarıda kullanabiliriz.



from math import *
islem=int(input("1 :\tfaktoriyel alma\n2 :\tlog hesaplama\n3 :\tkarakök alma\nişlemi seçiniz :\t"))
sayi=int(input("sayıyı yazınız."))
if(islem==1):
    print(factorial(sayi))
elif(islem==2):
    print(log(sayi))
elif(islem==3):
    print(sqrt(sayi))
else:
    print("yalnış değer girdiniz.")



import random
import time
print("sayı tahmin oyunu\n1 ile 40 arasında ki sayıyı tahmin edin.")
rastgele_sayi=random.randint(1,40)
tahmin_hakki=10
while True:
    tahmin=int(input("tahmininz :\t"))

    if (tahmin<rastgele_sayi):
        print("kontrol ediliyor...")
        time.sleep(2)

        print("daha yüksek bir sayı yazın.")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayi):
        print("kontrol ediliyor...")
        time.sleep(2)

        print("daha düşük bir sayı yazın.")
        tahmin_hakki-=1
    else:
        print("kontrol ediliyor...")
        time.sleep(2)
        print("doğru tahmin :\t",rastgele_sayi)
        break
    if (tahmin_hakki==0):
        print("tahmin hakkınız bitti.")
        print("sayı :\t",rastgele_sayi)
        break



# modüller sayesinde başka sayfalarda yazdığımız fonksyonları çağırabilliriz.
"   -1 modüller sayfası    `"

def naber():
    print("naber")
def mutlak(numara):

    if (numara<0):

        return -numara
    return numara


"   -2 diğer sayfa  "
#import modüller
#print(modüller.mutlak(-11))
#   çıktı
#   11

#	yada

#from modüller import mutlak
#print(mutlak(-15))
#   çıktı
#   15
