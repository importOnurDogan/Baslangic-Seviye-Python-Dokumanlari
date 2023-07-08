# Ne zaman fonksiyon yazılır?
#   =  sık tekrar eden ya da uzun işlemlerden kurtulmak icin yazılır"

def selamla(isim="isimsiz"):
    print("selam :",isim)
selamla()
"varsayılan değer eklendi. fonksyon çağırılırken içine birşey girilmezse, varsayılan değer yazdırılır."

def Hi(name, age):
    print("Merhaba\t",name," you are ",age," years old.")
Hi("hakan",24)
Hi("Gokce",26)

def Deneme2(num2):
    return num2*num2*num2
result = Deneme2(5)
print(result)

def kare_al(x):
    print(x,"üzeri 3 =\t",x**3)
kare_al(3)


income = int(input("Gelirinizi giriniz:\t"))
spent = int(input("Harcamalarinizi giriniz:\t"))
def kontrol(a,b):
    if income>spent:
        print("yeterli")
    elif income == spent:
        print("equal")
    else:
        print("yetersiz")
kontrol(income,spent)


def lamba_hesaplama(isi, nem, sarj):
    print((isi+nem)/sarj)
lamba_hesaplama(98,200,45)

def direk_hesap(isi, nem, sarj):
    return (isi+ nem)/sarj
print(direk_hesap(25,40,70))

"Local ve Global değişkenler"
"fonksyonun içi local, geri kalan ise global değişkenler"
X = 10
y = 20

def carpma_yap(x,y):
    return x*y
print(carpma_yap(2,3))

x=[]
def eleman_ekle(y):
    x.append(y)
    print(str(y)+" =ifadesi eklendi")
eleman_ekle(5)

#   -------------------
#   -------------------

def toplama(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)
toplama(100,99,98)


def factoriel(numara):
    faktoriyel=1
    for i in range(1,numara+1):
        faktoriyel*=i
    print("faktöriyel:",faktoriyel)

sayi=int(input("sayı giriniz:\t"))
factoriel(sayi)


#   -------------------
#   -------------------
#   **RETURN**

def kokbul(a,b,c):
    delta=(b*b-4*a*c)
    if(delta<0):
        print("reel kök bulunamadı:")
        return

    x1=(-b-delta**0.5)/2*a
    x2=(-b+delta**0.5)/(2*a)

    return(x1,x2)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
sonuc=kokbul(a,b,c)
#kokbul(a,b,c)yazmak uzun olduğu için değer atanmış
print(sonuc)


#   ----------------
#   -------------------
#	VARSAYILAN DEĞERLER

def kayit(ad="bilgi yok",soyad=(),yas="bilgi yok",meslek="bilgi yok"):
    print("ad:{}\nsoyad:{}\nyas:{}\nmeslek:{}\n".format(ad,soyad,yas,meslek))
    print("kayıt oluşturuldu.")
kayit(ad="aga",yas=40)
#yapamadım
def kayit(ad="bilgi yok",soyad="bilgi yok",yas="bilgi yok",meslek="bilgi yok"):
    print("ad:{}\nsoyad:{}\nyas:{}\nmeslek:{}\n".format(ad, soyad, yas, meslek))
    print("kayıt oluşturuldu.")
    kayit(input(kayit.format()))

#   ----------------
#   -------------------
#	---GEOMETRİK ŞEKİL YAPMA---

def geometri(sekil):
    if len(sekil)==3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        if(a+b)>c and (a+c)>b and(b+c)>a:
            if (a==b)and(a==c)and(b==c):
                print("eşkenar üçgen")
            elif(a==b)or(a==c)or(b==c):
                print("ikizkenar üçgen")
            else:
                print("çeşitkenar")
        else:
            print("üçgen belirtmiyor")

    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if (a==b)and(a==c)and(a==d):
            print("kare")
        elif(a==c)and(b==d)or(a==b)and(c==d)or(a==d)and(b==c):
            print("dikdörtgen")
        elif(a+b+c>d)and(a+b+d>c)and(a+c+d>b)and(b+c+d>a):
            print("çeşitkenar dörtgen")
        else:
            print("herhangi bir şekil değil")

while(True):
    ksayisi=int(input("köşe sayınızı giriniz:"))
    if(ksayisi==3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometri((a,b,c))

    elif(ksayisi==4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geometri((a,b,c,d))
    else:
        print("tekrar giriniz.")
    break

#   ----------------
#   -------------------
#fonksyon kullanarak kısa ve uzun kenarı girilen dikdörtgenin alanını hesapla.

def ddkenalan(kk,uk):
    alan=kk*uk
    print("dikdÃ¶rtgenin alanÄ± :\t",alan)
    #return alan

kk=int(input("kÄ±sa kenarÄ± giriniz :\t"))
uk=int(input("uzun kenarÄ± giriniz :\t"))
ddkenalan(kk,uk)

alan=ddkenalan(kk,uk)

#   ----------------
#   -------------------

def faktoriyel(sayi):
    faktoriyel=1
    if (sayi ==0 or sayi==1):
        print("faktöriyell :\t",faktoriyel)
    else:
        while (sayi>1):
            faktoriyel*=sayi
            sayi -= 1
        print("faktöriyel :\t{}".format(faktoriyel))


a=int(input("sayıyı girin :\t"))
faktoriyel(a)

#   ----------------
#   -------------------

a=int(input("sayı giriniz :\t"))
b=int(input("ikinci sayıyı gir :\t"))
def carpma(a):
    print("ilk fonksyon çalıştırıldı.")
    return a*2
def toplama (b):
    print("ikinci fonksyon çalıştırıldı.")
    return b+10
def toplama2 (a):
    print("üçüncü fonksyon çalıştırıldı.")
    return a+b
print(toplama2(toplama(carpma(b))))

#	-carpma(b)- baştaki fonlsyonuna döndüğü zaman -a- -b- ye eşitleniyor.
