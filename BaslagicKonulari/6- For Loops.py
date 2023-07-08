Liste = [3,5,7,9]
for i in Liste:
    print(i+1)


for i in range(1,20):
    print("*"*i)


# Maaslara zaam yap.
Liste2 = [1000,2000,3000,4000]
for i in Liste2:
    i = i + ((i/10)*2)
    print("New salaries:\t",i)

def NewSalaries(x):
    print(x + ((x/10)*2))
for a in Liste2:
    NewSalaries(a)



maaslar = [1000,2000,3000,4000,5000]
def reise(a):
    if a<= 3000:
        print("Yeni maas:\t", a + (a/10)*2)
    else:
        print("Yeni maas:\t", a + (a/10))
for i in maaslar:
    reise(i)



toplam=0
liste=[1,2,3,4,5,6,7]
eleman=0
for eleman in liste:
    toplam+=eleman
    a=eleman
print("toplam :{} ve eleman :{}".format(toplam,eleman))
print(toplam)



liste=[(1,2),(3,4),(5,6),(7,8)]
for (i,j)in liste:
    print("i :{} ve j :{}".format(i,j))



liste={"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in liste:
    print(eleman)

liste={"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in liste.values():
    print(eleman)

liste={"bir":1,"iki":2,"üç":3,"dört":4}
for eleman in liste.items():
    print(eleman)




for i in range(1,10,2):
    print(i)
faktoriyel=1
while True:
    sayi=int(input("negatif olmayan bir sayı giriniz:\t"))
    if(sayi<=0):
        print("pozitif bir sayı girmelisiniz.")
    else:
        for i in range(1,sayi+1):
            faktoriyel *=i
        print("faktöriyel:",faktoriyel)
        break


### continue kullanıldığında işlem yapmadan döngünün başına gider.###
listeler=[2,3,4]
for i in range(0,10):
    if(i in listeler):
        continue
    print(i)



liste=[1,2,3,4,5,6,7,8,9]
for i in liste:
    if(i==4 or i==7):
        continue
    print("i :\t",i)



maaslar=[10,30,70,80,10,50,90,25]
maaslar.sort()
print("YeniHali =\t",maaslar)
for i in maaslar:
    if i == 50:
        print("kesildi((")
        break
    print(i)




#   range komutu
sonuc=[]
for i in range(1,100):
    for b in range(2,i):
        if(i%b==0):
            break
    else:
        sonuc.append(i)
print(sonuc)



#virgÃ¼lle girilen sayÄ±larÄ±n toplanÄ±p ortalamasÄ±nÄ±n alÄ±nmasÄ±.

numaralar=input("virgÃ¼l ile sayÄ±larÄ± giriniz:\t")
print("girdiÄŸiniz sayÄ±lar.{}".format(numaralar))
#print("girdiÄŸiniz sayÄ±lar",numaralar)

numaralar2=numaralar.split(",")
toplam=0
for n in numaralar2:
    toplam = toplam+int(n)
print("sayÄ±larÄ±n ortalamasÄ±:{0:.2f}".format(toplam/len(numaralar2)))




a=int(input("ilk sayÄ±yÄ± giriinz =\t"))
b=int(input("ikinci sayÄ±yÄ± giriniz =\t"))
c=int(input("aralÄ±k deÄŸerini giriniz =\t"))

toplam=0
for i in range(a,b,c):
    toplam=toplam+i
print("sonuÃ§ {}".format(toplam))
#girilen deÄŸerler arasÄ±ndaki sayÄ±larÄ± toplar




#a ve b deÄŸerleri arasÄ±ndaki sayÄ±larÄ±n 4 ve 6 nÄ±n ortak katÄ± olan sayÄ±larÄ± yazdÄ±ran program.
a = int(input("ilk sayÄ±yÄ± giriniz ="))
b = int(input("ikinci sayÄ±yÄ± giriniz ="))

for i in range(a, b):
    if (i % 4 == 0 and i % 6 == 0):
        print(i)
    else:
        print("ortak bÃ¶len bulunamadÄ±.")
    break
#   numaralar = (i % 4 == 0) and (i % 6 == 0)
#   print(int("numaralar ={}".format(numaralar)))




#0 ile 50 arasÄ±nda rastgele oluÅŸturulan 10 elemanlÄ± dizideki en bÃ¼yÃ¼k ve en kÃ¼Ã§ÄŸk sayÄ±yÄ± bulan program
from random import randint

sayilar=[]
for i in range(0,10):
    rand=randint(0,50)
    sayilar.append(rand)
    print(rand)

minNumber=sayilar[0]
maxNumber=sayilar[0]

for i in range(0,10):
    if minNumber>sayilar[i]:
        minNumber=sayilar[i]
    if maxNumber<sayilar[i]:
        maxNumber=sayilar[i]

print("dizideki en bÃ¼yÃ¼k deÄŸer  :{0}".format(maxNumber))
print("dizideki en kÃ¼Ã§Ã¼k deÄŸer  :{0}".format(minNumber))