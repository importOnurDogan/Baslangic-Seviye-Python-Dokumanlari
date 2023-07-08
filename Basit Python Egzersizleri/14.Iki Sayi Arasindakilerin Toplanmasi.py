#girilen 2 sayı arasındaki sayıların toplanması.

sayi1=input("ilk sayıyı gir :\t")
sayi2=input("ikinci sayıyı gir :\t")

toplam=0

for i in range(int(sayi1),int(sayi2)):
    toplam=i+toplam
print("toplam :{0}\t".format(toplam))
