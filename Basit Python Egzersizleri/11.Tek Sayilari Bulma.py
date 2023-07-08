#1 den girilen sayıya kadar olan tek sayıları listeleme. listeye attırdım.

sayi=int(input("ilk sayıyı giriniz :\t"))
c=list()

for i in range (1,sayi):
    if(i%2!=0):
        c.append(i)
print("liste :\t",c)
