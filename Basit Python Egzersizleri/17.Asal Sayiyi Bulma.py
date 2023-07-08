#girilen sayı asal mı değil mi

sayi=int(input("sayı giriniz :\t"))
a=0

for i in range (2,sayi):
    if (sayi%i==0):
        a+=1
        #break   yazılabilir
if a!=0:
    print("asal değil")
else:
    print("asal")

#   OR

a=int(input("sayı giriniz :\t"))
b=0

for i in range(2,a+1):
    if((a-1)%i==0):
        b+=1
    else:
        continue
if(b==0):
    print("bu sayı asal sayıdır :\t{}".format(a))
else:
    print("{} asal sayı değildir.".format(a))

#       OR

def asal(sayi):
    a = 0
    for i in range(2,sayi):
        if (sayi%i==0):
            a+=1
        else:
            continue
    if (a == 0):
        print("bu bir asal sayıdır.")
    else:
        print("bu asal sayı değildir.")
while True :
    b = input("Çıkmak için -q- ya basınız.\nBir sayı giriniz :\t")
    if (b=="q"):
        print("çıkış yapıldı.")
        break
    asal(int(b))
