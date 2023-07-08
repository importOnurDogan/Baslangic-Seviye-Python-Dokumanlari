#FONKSYON KULLANARAK KENARLARI VERİLEN DİKDÖRTGENİN ALANINI HESAPLA.

def ahesaplama (uk,kk):
    alan=uk*kk
    print("dikdörtgenin alanı :\t",alan)
    return (alan)

kk=int(input("kısa kenarı yazını :\t"))
uk=int(input("uzun kenarı yazınız :\t"))

ahesaplama(uk,kk)
