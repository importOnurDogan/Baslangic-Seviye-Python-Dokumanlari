#girilen 2 sayı arasındaki çift sayıları yazdır. listeye atarak yaptir.

a=int(input("ilk sayıyı giriniz :\t"))
b=int(input("ikinci sayıyı giriniz :\t"))
c=list()

for i in range (int(a),int(b)):
    if (i%2==0):
        c.append(i)
    else:
        continue
print("liste :\t",c)
