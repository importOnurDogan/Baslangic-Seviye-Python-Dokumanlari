"	---- DOSYA AÇMA ----      "
#dosya açma --open-- fonksyonuyla olur.bu fonksyon 2 parametre alır.ilki dosyanın adı, ikincisi dosyanın ne yapılacağı mod dur.


"	 1.mod 'w'      "
#dosyayı yapar ve içine birşeyler yazdırır. eğer halihazırda bir dosya varsa eskisini silip yanisini açar.

file=open("bilgiler.txt","w")
print(file.write("onur doğan"))
file.close()
#   ÇIKTI	= 10
file=open("bilgiler.txt","w",encoding="utf-8")
#,encoding="utf-8")	=   türkçe karakterler yazabilmemizi sağlar



"    2.mod	'r'     "
#olan bir dosyayı açıp içindekileri almamızı, okumamızı sağlar.

dosya=open("merhaba","r")
print(dosya.read())
#	ve
#print(dosya.readLine())
#	ve
#print(dosya.readLines())



with open("merhaba","r") as dosya:
    print(dosya.read())
#   bu bloktan sonra dosya tamamen kapanır.



#	dosya.seek() --> dosyada istenilen yere gider.
with open("merhaba","r") as dosya:
    dosya.seek(2)
    print(dosya.read(3))


#   kaydın 2 kelimesinden başladı ve 3 tane karakter yazdırdı.
with open("merhaba","r") as dosya:
    dosya.seek(2)
    str=dosya.read(2)
    dosya.seek(6)
    str2=dosya.read(1)
    print(str,str2)
#metnin istenilen yerine istenilen değer yazdırılabilir.
#liste.insert(kaçıncı index istersek,"ornek str")



"	*** 3.mod 'a' "
#olan bir dosyanın içindeki bilgileri değiştirmez sadece ekleme yapar.eğer dosya yoksa yeni açar.


# BAŞKA SAYFALAR AÇABİLİYORUZ.
#---MODULİNTERNET.py--- SAYFASINDA
dosya=open("deneme","w")
dosya.write("ciguli")
#	ÇIKTI
#---deneme adlı yeni bir sayfa oluştu ve içinde
#ciguli
#*** mod değiştiği zaman kayıt edilen değişmiyor aksine ekleniyo.***

dosya=open("deneme","a")
dosya.write(" aga")
#	ÇIKTI
#ciguli aga
