#Create a program that asks to user that enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
#(Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines.

from datetime import date

ad=input("adınızı giriniz :\t")
yas=int(input("yaşınızı giriniz :\t"))
kopya=int(input("kaç adet kopya istiyorsunuz \t"))
today = date.today()
surec=100-yas
print("sayın :\t",ad,"\n",today.year+surec,"yılın da 100 yaşında olacaksınız.")
a=0
kpy=1
while (True):
    print("kopya",kpy,"sayın :\t",ad,"\t",today.year+surec,"yılın da 100 yaşında olacaksınız.")
    a+=1
    kpy+=1
    if(a<kopya):
        continue
    else:
        break

