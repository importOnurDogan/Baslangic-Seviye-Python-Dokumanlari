# tam bölenleri bulma

a=int(input("sayı giriniz :\t"))
b=[]

for i in range(1,a):
    if(a%i==0):
        b.append(i)
    else:
        continue
print("bu sayının tam bölenleri :\t{}".format(b))
