    #VERI YAPILARI

#LISTELER = degisebilir, sirali, kapsayici
#TUPLE = degistirilemez, sirali, kapsayici
#SOZLUK = degistirilebilir, sirasiz, kapsayici
#SETLER = degistirilebilir, sirasiz, kapsayici


a=int(input("birinci sayıyı giriniz:"))
b=int(input("ikinci sayıyı giriniz:"))
#string olarak alınan değerlerin integer e dönüştürülmesi
ilksayi=a
ikincisayi=b
toplam=ilksayi+ikincisayi
fark=ilksayi-ikincisayi
carpim=ilksayi*ikincisayi
bolum=ilksayi/ikincisayi
mod=ilksayi%ikincisayi
print("girdiğiniz sayılar :{},{}".format(a,b))
print("toplam :".format(toplam))
print("fark :{}".format((fark)))
print("carpim :{}".format(carpim))
print("bolum :{}".format(bolum))
print("mod{}{} :{}".format(a,b,mod))



# 1 - Liste Olusturma.

notlar = [90,80,70,60]
print(type(notlar))

genis_list = ["a",19.4,100,notlar]
print(len(genis_list))

print(type(genis_list[1]))
print(genis_list[3])

tum_iste = [notlar, genis_list]
print(tum_iste)

" ------------ "
'Eleman Islemleri'
liste = [10,20,30,40,50]
print(liste[0], liste[3])
print(liste[0:2])
print(liste[:2])

yeni_liste = ["a",10,[20,30,40,50]]
print(yeni_liste[2][3])

" ------------ "
'Eleman Degistirme'
Liste2 = ["a","b","c","d"]
Liste2[2] = "w"
print(Liste2)
Liste2[0:2] = "k","t"
print(Liste2)

Liste2 = Liste2 + ["p"]
del Liste2[0]
print(Liste2)

" ------------ "
'Liste Metodlari'
liste.append("mom")
print(liste)
liste.remove(10)
print(liste)

" ------------ "
'Insert'
A4 = ["1","2","3"]
A4.insert(0,"Banu")
print(A4)

A4.insert(len(A4),"Selen")
print(A4)
A4.pop(2)
print(A4)

#Other list methods

'Count'
List3 = ["A","B","C","D","C"]
print(List3.count("C"))
'copy'
yedek_List3 = List3.copy()
'Extend'
List3.extend(["a",10,11])
print(List3)
'Index'
print(List3.index("D"))
'Reverse'
print(List3.reverse())



#2 - TUPLE OLUSTURMA

t = ('w',2,3,4,['b',9,8,7])
print(type(t))

# 3 -   DICTIONARY OLUSTURMA

sozluk = {'a':2,
          'b':3,
          "c":4}
print(sozluk["b"])

sozluk['a']= 55
sozluk['d'] = 11
print(sozluk)

# 4 - SETLER

L = ["A","B","C","D","C"]
print(set(L))

s = set(L)
s.add("O")
s.remove("A")
print(s)

set1 = [2,3,4,5]
S1 = set(set1)
set2 = [2,4,6]
S2 = set(set2)

print(S1.intersection(S2))

S3 = S1.union(S2)
print(S3)

