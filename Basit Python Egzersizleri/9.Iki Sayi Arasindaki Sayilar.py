#girilen iki sayı arasındaki sayıları sıralama

a=int(input("ilk sayıyı giriniz :\t"))
b=int(input("ikinci sayıyı giriniz :\t"))
c=list()

for i in range (int(a),int(b)):
    c.append(i)
print("liste :\t",c)
