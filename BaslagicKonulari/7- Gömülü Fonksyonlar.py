"   MAP FONKSYONU       "
# map ile bir liste içerisindeki elamanların
# parametre olarak verilen fonksiyonla yapılandırılmasını sağlayabiliriz

def double(x):
    return 2*x
map(double,[2,3,4,5])
print(list(map(double,[2,3,4,5])))
print(list(map(lambda x :x **2,(2,3,4,5))))



liste1=(5,6,7)
liste2=(7,8,9)
print(list(map(lambda x,y : x + y,liste1,liste2)))
#	 ÇIKTI
#[4, 6, 8, 10]
#[4, 9, 16, 25]
#[12, 14, 16]



"   REDUCE FONKSYONU   "

from functools import reduce
def toplama(x,y):
    return x+y
print(reduce(toplama,[10,15,40,90]))
print(reduce(lambda x,y :x*y,[5,3,9,2]))



def maxsimum(x,y):
    if(x>y):
        return x
    else:
        return y
print(maxsimum(3,5))
print(reduce(maxsimum,[2,-60,90,41]))
#  fonksyonu listenin ilk 2 elemanına uygular. sonra çıkan sonucu
#  listenin 3. sonra 4. elamanına uygulayarak liste bitene kadar devam eder.



"   FİLTER FONKSYONU    "

# FİLTER SADECE TRUE SONUÇ ÇIKARAN DEĞERLERİ ALIP DÖNER.

print(list(filter(lambda x : x%2==0,[1,2,3,4,5,6,7,8,9])))

def asal_mi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while (i<x):
            if(x%i==0):
                return False
            i+=1
        return True

print(asal_mi(100))
print(list(filter(asal_mi,range(1,100))))
#	ÇIKTI
#[2, 4, 6, 8]
#False
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]




"   ZİP FONKSYONU   "

liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
i=0
sonuc=list()
while((i<len(liste1))and(i<len(liste2))):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)
#   yada zip fonksyonu kullanılabilir.
print(list(zip(liste1,liste2)))



liste3=[1,2,3,4]
liste4=["a","b","c","d"]
for i,j in zip(liste3,liste4):
    print(i,j)
# birden fazla listenin elemanlarını alarak başka bir liste yapar.
#	ÇIKTI
#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
#[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
#1 a
#2 b
#3 c
#4 d



"   ENUMERATE FONKSYONU     "

#listedeki elemanlara numara vererek yeni bir liste yapar.
liste=["a","b","c","d"]
print(list(enumerate(liste)))
for i,j in enumerate(liste):
    if(i%2==0):
        print(j)
#	ÇIKTI
#[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
#a
#c

