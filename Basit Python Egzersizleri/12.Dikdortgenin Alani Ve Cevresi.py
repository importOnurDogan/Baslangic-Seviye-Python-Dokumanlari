#kenarları girilen dikdörtgenin alanı ve çevresi

uzunk1=int(input("birinci uzun kenarı gir :\t"))
uzunk2=int(input("ikinci uzun kenarı gir :\t"))
kisak1=int(input("birinci kısa kenarı gir :\t"))
kisak2=int(input("ikinci kısa kenarı gir :\t"))

if (uzunk1==uzunk2)and (kisak1==kisak2):
    print("çevresi =\t",uzunk1+uzunk2+kisak1+kisak2,"\nalanı =\t",uzunk1*kisak1)
#yada
kenar1=int(input("1. kenarı giriniz :\t"))
kenar2=int(input("2. kenarı giriniz :\t"))
kenar3=int(input("3. kenarı giriniz :\t"))
kenar4=int(input("4. kenarı giriniz :\t"))

if ((kenar1<=kenar2+kenar3+kenar4)and(kenar2<=kenar1+kenar3+kenar4)and(kenar3<=kenar1+kenar2+kenar4)and(kenar4<=kenar1+kenar2+kenar3)and(kenar1,kenar2,kenar3,kenar4>0)):
    print("çevre :\t",kenar1+kenar2+kenar3+kenar4)
else:
    print("yanlış değerler girdiniz.")
