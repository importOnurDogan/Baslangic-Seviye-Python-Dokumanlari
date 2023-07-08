i = 0
while (i < 10):
    print("i nin değeri:\t", i)
    i += 1
#    ÇIKTI
#i nin değeri:	 0
#i nin değeri:	 1
#i nin değeri:	 2
#i nin değeri:	 3
#i nin değeri:	 4
#i nin değeri:	 5
#i nin değeri:	 6
#i nin değeri:	 7
#i nin değeri:	 8
#i nin değeri:	 9
#   -------------

ad = "onur"
sfr = "456"
while (True):
    kullanici = input("adınızı giriniz:\t")
    parola = input("parolayı giriniz:\t")
    if ((ad == kullanici) and (sfr == parola)):
        print("hoşgeldiniz")

    elif ((ad != kullanici) and (sfr == parola)):
        print("kullanıcı adını hatalı girdiniz.")
    elif ((ad == kullanici) and (sfr != parola)):
        print("şifreyi yanlış girdiniz.")
    else:
        print("adı ve parolayı yanlış girdiniz.")
        break
#   ------------------

# metni harflerine ayÄ±rma
isim = input("metni girin =\t")
sayac = 0
while sayac < len(isim):
    print(isim[sayac])
    sayac += 1
print("harflerine ayÄ±rdÄ±m.")
# else:
#    print("harflerine ayÄ±rdÄ±m.")
#   -------------

ad = "onur"
sfr = "456"
while (True):
    kullanici = input("adını giriniz:\t")
    parola = input("parola giriniz:\t")
    if ((ad == kullanici) and (sfr == parola)):
        print("hoşgeldiniz")
        break
    elif ((ad != kullanici) and (sfr == parola)):
        print("kullanıcı adını hatalı girdiniz.")
    elif ((ad == kullanici) and (sfr != parola)):
        print("şifreyi yanlış girdiniz.")
    else:
        print("adı ve parolayı yanlış girdiniz.")
        print("yeni ad ve şifre istermisin?(E/H)")
        cevap = input()
        if (cevap == "E"):
            add = input("yeni adın:\t")
            ad = add
            sfrr = input("yeni şifren:\t")
            sfr = sfrr
            print("şimdi tekrardan giriş yapmayı deneyelim.")
            kullanici = input("adınızı giriniz:\t")
            parola = input("parolayı giriniz:\t")
            if ((add == kullanici) and (sfrr == parola)):
                print("bilgiler doğru.hoşgeldiniz")
            else:
                print("gene hatalı giriş yaptınız.")

    print("ad ve şifrenizi hatırladığınız zaman tekrar deneyiniz.")
    break
#    -----------------

import time
hour = int(input("saat.\t"))
minute = int(input("dakika:\t"))

while True:
    saat = time.localtime(time.time())

    if (hour == saat.tm_hour and minute == saat.tm_min):
        print("alarm caldÄ±\nsaat=\t", saat.tm_hour, ":", saat.tm_min)
        break
    else:
        pass
print("bitti.")
#   ---------------

i = 0
while (i < 10):
    if (i == 2):
        continue
    print(i)
    i += 1
#    ÇIKTI
#0
#1
#   -----------------

# 0 dan 100 e kadar 3Ã¼n katÄ± olan Ã§ift sayÄ±larÄ±, yazdÄ±ran program.
sayac = 0
while (sayac < 100):
    sayac = sayac + 2
    if sayac % 3 == 0:
        print(sayac)
#   --------------------

    # udemy dersler "while"
i = 0
while (i < 20):
    i += 1
    print(i)
#    ----------------------

liste = [1, 2, 3, 4, 5]
index = 0
while (index < len(liste)):
    print("index :", index, "liste elemanı :", liste[index])
    index += 1
#   ÇIKTI
#index : 0 liste elemanı : 1
#index : 1 liste elemanı : 2
#index : 2 liste elemanı : 3
#index : 3 liste elemanı : 4
#index : 4 liste elemanı : 5
#   ----------------------

# udemy dersler "break ve continue"
i = 0
while (i < 10):
    if (i == 5):
        break
    print("i :\t", i)
    i += 1
#    --------------------

while True:
    print("programdan çıkmak için -q- harfini kullanın.")
    isim = input("adınızı giriniz :\t")
    if (isim == "q"):
        print("programdan çıkılıyor")
        break
    print("isminiz :\t", isim)

    ### --while True-- kullanılırken bir sonlandırma komutu kullanılmazsa (break gibi) döngü sozsuza kadar devam eder.
#    --------------------

i = 0
while (i < 10):
    if (i == 3):
        continue
    print(i)
    i += 1
    ###3 ten sonra hep başa döndüğü için sonsuz döngüye girip hiçbirşey yazdıramıyor.
#    -----------------------

#    HESABA GİREBİLME PROGRAMI

kad = "aga"
kparola = 456
denemeh = 3

while True:
    a = input("kullanıcı adınızı giriniz:\t")
    b = int(input("şifrenizi giriniz :\t"))
    if (kad != a and kparola != b):
        print("adınızı ve şifrenizi yanlış girdiniz.")
        denemeh -= 1
        if (denemeh == 0):
            print("deneme hakkınız doldu.")
            break
    elif (kad == a and kparola != b):
        print("şifrenizi yanlış girdiniz.")
        denemeh -= 1
        if (denemeh == 0):
            print("deneme hakkınız doldu.")
            break
    elif (kad != a and kparola == b):
        print("adınızı yanlış girdiniz.")
        denemeh -= 1
        if (denemeh == 0):
            print("deneme hakkınız doldu.")
            break
    else:
        print("hoşgeldiniz.")
        break


