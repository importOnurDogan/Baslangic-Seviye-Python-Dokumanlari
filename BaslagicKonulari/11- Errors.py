try:
    a=int(23)
    print("program çalışıyor.")
except ValueError:
    print("hata oluştu.")
print("program sona erdi.")


try:
    a=int("aga")
    print("program çalışıyor.")
except ValueError:
    print("hata oluştu.")
print("program sona erdi.")


try:
    a=int(input("ilk sayıyı giriniz :\t"))
    b=int(input("ikinci sayıyı giriinz :\t"))
    print(a/b)
except ValueError:
    print("***lütfen int karakter giriniz.***")
except ZeroDivisionError:
    print("***sayı 0 a bölünemez.***")
print("program sona erdi.")


try:
    a=int(input("ilk sayıyı giriniz :\t"))
    b=int(input("ikinci sayıyı giriinz :\t"))
    print(a/b)
except ValueError:
    print("***lütfen int karakter giriniz.***")
except ZeroDivisionError:
    print("***sayı 0 a bölünemez.***")
finally:
    print("finally bloğu hep çalışır.")
print("program sona erdi.")


def terscevir(s):
    if(type(s) != str):
        raise ValueError("lütfen string bir değer gönderin.")
    else:
        return s[::-1]
print(terscevir("python."))


try:
    print(terscevir(12))
except ValueError:
    print("fonksyon hata verdi.")
#	------------------------

#Problem 1
#Elinizde stringlerin bulunduğu bir liste bulunduğunu düşünün.
#liste = ["345","sadas","324a","14","kemal"]
#Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.

liste = ["345","sadas","324a","14","kemal"]
liste2 = []
try:
    def listem():
        for i in liste:
            for a in i.split():
                if (a=="0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9"):
                    liste2.append(i)
except ValueError:
    print("***sayı yok.***")
print(liste2)

##### doğrusu

liste = ["345", "sadas", "324a", "14", "kemal"]
for eleman in liste:

    try:
        eleman = int(eleman)
        print(eleman)
    except:
        pass
#	-----------------------

#Problem 2
#Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
#Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
#Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın.


def sayilar():
    for i in listem:
        if i%2==0:
            return i
        elif i%2!=0:
            raise ValueError("ValueError.")
#print("çift sayılar :\t",i)
listem=(1,2,3,4,5,6,7,8,9)
sayilar()

#### doğrusu

def cift_mi(sayi):
    if (sayi % 2 == 0):
        return sayi
    else:
        raise ValueError

liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass