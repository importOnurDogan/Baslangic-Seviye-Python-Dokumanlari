#girilen iki değer arasındaki tek ve çift sayıları ayrı toplayıp yazdır.

sayi1=int(input("ilk sayıyı giriniz :\t"))
sayi2=int(input("ikinici sayıyı giriniz :\t"))

tek=0
cift=0

for i in range(sayi1,sayi2):
    if i%2!=0:
        tek+=i
    elif i%2==0:
        cift+=i
print("tek sayıların toplamı :\t{0}\nçift sayıların toplamı :\t{1}".format(tek,cift))
