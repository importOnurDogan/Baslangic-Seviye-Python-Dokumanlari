#   IF - ELSE       Karar Yapilari

is_male = False
if is_male:
    print("you are a male")
else:
    print("you are a woman")



is_woman = True
is_tall = True
is_blonde = False
if is_woman or is_tall:
    print("this woman is tall")
else:
    print("you neither tall nor woman")

if is_blonde and is_woman:
    print("she is blonde")
else:
    print("you are either not woman or not blonde or both")



is_male = True
is_short = False
if is_male and is_short:
    print("you are a short man")
elif not(is_male) and is_short:
    print("You are not a man")
elif is_male and not(is_short):
    print("You are a tall man")
else:
    print("you are neither man nor short")



def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    elif num3>=num2 and num3>=num1:
        return num3
print(max_num(5,5,6))


###########################
###########################


print("bugün kü sıcaklığı giriniz: ")
sicaklik=input()
karar="bugünkü aktivite"

if int(sicaklik)>30:
    karar=karar+" yüzme"
elif int(sicaklik)>20:
        karar=karar+" voleybol"
elif int(sicaklik)>10:
            karar=karar+" kafe ye gitmek"
else:
    karar=karar+" evde kalmak"

print(karar)
"   ÇIKTI"
"bugün kü sıcaklığı giriniz:"
"24"
"bugün kü aktivite voleybol"




cevap="ciguli"
print("kullanıcı adını giriniz :")
isim=input()

if cevap==isim:
    print("işlem başarılı")
else:
    print("yanlış değer. 2 hakkınız kaldı")
    isim=input()
    if cevap==isim:
        print("işlem başarılı")
    else:
        print("yanlış değer.1 hakkınız kaldı")
        isim=input()
        if cevap==isim:
            print("işlem başarılı")
        else:
            print("yanlış değer, giriş hakkınız doldu")
"   ÇIKTI"
"kullanıcı adını giriniz :"
"ciguli"
"işlem başarılı"




yas=int(input("yaşınızı girin: "))
if  yas<18:
    print("giremezsiniz")
else:
    print("girebilirsiniz")

"***(İF VE ELSE LER AYNI HİZADA OLMALI)***"
"***elif kodu eger önceden yazılan if kodu olmazise çalışır.ama eğer hep (İF)yazarak denersek doğru olan bütün(İF)ler çalışır"
"ÇIKTI"




sayi1=int(input("1. sayÄ±yÄ± gir:\t"))
sayi2=int(input("2. sayÄ±yÄ± gir:\t"))
secim=int(input("secimini yap:\n1. toplama\n2. cikarma\n3. carpma\n4. bolme\nsecimin: "))

if secim==1:
    print("sonuc =\t",sayi1+sayi2)
elif secim==2:
    print("sonuc =\t",sayi1-sayi2)
elif secim==3:
    print("sonuc =\t",sayi1*sayi2)
elif secim==4:
    print("sonuc =\t",sayi1/sayi2)
else:
    print("hatalÄ± deger girdiniz")




puan = int(input("notunuzu giriniz: "))
if 70<puan<90:
    print("BB")
elif 50<puan<70:
        print("CC")
elif puan<50:
            print("FF")
else:
                    print("AA")
"   ÇIKTI"
"notunuzu giriniz: 95"
"AA"




ad="asd"
parola="45623"
a=input("kullanıcı adınızı giriniz: ")
b=input("parolanızı giriniz: ")

if (a == ad) and (b == parola) :
    print("kullanıcı bilgileri doğru")
else:
    print("hata var.lütfen bilbileri tekrardan giriniz")
"   ÇIKTI"
"kullanıcı adınızı giriniz: asd"
"parolanızı giriniz: 45623"
"kullanıcı bilgileri doğru"




ad="asd"
parola="45623"
a=input("kullanıcı adınızı giriniz: ")
b=input("parolanızı giriniz: ")

if (a == ad) and (b == parola) :
    print("kullanıcı bilgileri doğru")
elif (a==ad) and (b!=parola):
    print("parola hatalı.")
elif (a!=ad)and(b==parola):
    print("ad hatalı")
else :
    print("ad ve parola hatalı")
"   ÇIKTI"
"kullanıcı adınızı giriniz: asd"
"parolanızı giriniz: 45623"
"kullanıcı bilgileri doğru"




sinir= 500
magaza_adi=input("Mağaza adını giriniz :\t")
gelir=int(input("Geliriniz nedir? :\t"))

if gelir>sinir:
    print("Tebrikler: ",magaza_adi," promosyon kazandınız.")
elif gelir<sinir:
    print("Üzgünüz, yetersiz bakiye ",gelir)
else:
    print("takibe devam.")