#FOKSYON KULLANARAK YARIÇAPI GİRİLEN DAİRENİN ALANINI HESAPLA

def daire (yaricap):
    alan = yaricap*yaricap*3.141
    # YARİCAPLAR YERİNE r DE YAZILABİLİRDİ.
    print("alan :\t",alan)


r=float(input("yarı çapı gir :\t"))
daire(r)
