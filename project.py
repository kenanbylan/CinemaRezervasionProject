import time 


#global degişkenler tüm fonksiyonlar tarafından erişilen değişkenler 
#                    #     1   2    3     4
KategoriKoltukSayisi = [100, 100, 100, 100]
kategoriCiro = [0, 0, 0, 0]
ToplamCiro = 0
ToplamSatılanBilet = 0

fiyatMatris = []
matris = []

kategori1SatilanBilet = 0
kategori2SatilanBilet = 0
kategori3SatilanBilet = 0
kategori4SatilanBilet = 0


#belirtilen satırı okuma
def dosyaOkuSatir(satir):
    with open("indirim.txt", "r") as file:
        for i in range(satir):
            result = file.readline()
        file.close()
    return result


#dosyadan fiyat listesini okuma 
kategori1fiyat = dosyaOkuSatir(2)
kategori2fiyat = dosyaOkuSatir(3)
kategori3fiyat = dosyaOkuSatir(4)
kategori4fiyat = dosyaOkuSatir(5    )

#fiyatları almak için split işlemi
kategori1fiyat =  kategori1fiyat.split("-")[-1]
kategori2fiyat =  kategori2fiyat.split("-")[-1]
kategori3fiyat =  kategori3fiyat.split("-")[-1]
kategori4fiyat =  kategori4fiyat.split("-")[-1]

#fiyat listesini matrise atama
fiyatMatris.append(kategori1fiyat)
fiyatMatris.append(kategori2fiyat)
fiyatMatris.append(kategori3fiyat)
fiyatMatris.append(kategori4fiyat)

#gelen string degerini int degerine çevirme
fiyatMatris = [int(i) for i in fiyatMatris] #string listesini int listesine çevirme


#baslangic durumu
def salonDurumu():
    for i in range(20):
        column = []
        for j in range(20):
            column.append("-")
        matris.append(column)

    print("Salonun durumu:")
    for i in range(20):
        for j in range(20):
            print(matris[i][j], end=" ")
        print()

salonDurumu()


def biletSayisi(n):
    print("Kategori", n, "için kalan bilet sayisi :", "KategoriKoltukSayisi"[n-1])


def toplamCiro():
    print("Toplam Ciro: ", ToplamCiro)



#acılıs sayfası 
print("Hoşgeldiniz")
while True:

    print("1- Bilet Al")
    print("2- Salon Durumu")
    print("3- Toplam Ciro")
    print("4- Kategori Bilet Durumu")
    print("5- Her şeyi sıfırla")
    print("6- Çikiş")

    secim = int(input("Seçiminiz: "))
    if secim == 1:
        print("1- Kategori 1")
        print("2- Kategori 2")
        print("3- Kategori 3")
        print("4- Kategori 4")
        
        kategori = int(input("Seçiminiz: "))

        if kategori == 1:
            print("Kategori 1")
            print("Kategori 1 için kalan bilet sayisi :", KategoriKoltukSayisi[0] )
           # print("Kategori 1 için bilet fiyatı: 10 TL")
            biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
            satılanBilet = biletAdet
            kategori1SatilanBilet = satılanBilet;
            if biletAdet > 100 or biletAdet <= 0 : #kategori- 1 için 100 bilet var 
                print("Kategori 1 için uygun bilet kalmamıştır")
            else:
                print("Kategori -1 için", biletAdet, "bilet rezerve ediliyor...")
                time.sleep(1)
                for i in range(10):
                    for j in range(5,15):
                        if biletAdet > 0:
                            matris[i][j] = "X"
                            biletAdet -= 1

            
                KategoriKoltukSayisi[0] -= biletAdet #kalan bilet sayısı için yapıldı.
                print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                for i in range(10):
                    for j in range(5,15):
                        if matris[i][j] == "X":
                            print(i+1,"-",j+1, end="  ")
                print()
                print("Kategori 1 için kalan bilet sayısı:", 100 - satılanBilet)
                kategoriCiro[0] = satılanBilet * fiyatMatris[0]
                ciro = kategoriCiro[0]
                print("Kategori 1 için gelir:",ciro, "TL")


                print("Salonun durumu:")
                for i in range(20):
                    for j in range(20):
                        print(matris[i][j], end=" ")
                    print()
            
        
        elif kategori == 2:
            print("1- Kategori 2 Sol blok")
            print("2- Kategori 2 Sağ blok")
            kategori2 = int(input("Seçiminiz: "))

            if kategori2 == 1:
                print("Kategori 2 Sol blok")
                print("Kategori 2 için kalan bilet sayisi :", KategoriKoltukSayisi[1] )
                biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
                satılanBilet = biletAdet
                kategori2SatilanBilet = satılanBilet;
                if biletAdet > 100 or biletAdet <= 0 :
                    print("Kategori 2 için uygun bilet kalmamıştır")
                else:
                    print("Kategori -2 için", biletAdet, "bilet rezerve ediliyor...")
                    time.sleep(1)
                    for i in range(10):
                        for j in range(5):
                            if biletAdet > 0:
                                matris[i][j] = "X"
                                biletAdet -= 1

            
                    KategoriKoltukSayisi[1] -= biletAdet
                    print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                    for i in range(10):
                        for j in range(5):
                            if matris[i][j] == "X":
                                print(i+1,"-",j+1, end="  ")
                    print()
                    print("Kategori 2 için kalan bilet sayısı:", 100 - satılanBilet)
                    kategoriCiro[1] = satılanBilet * kategori1fiyat
                    ciro = kategoriCiro[1]
                    print("Kategori 2 için gelir:",ciro, "TL")
                    print("Salonun durumu:")
                    for i in range(20):
                        for j in range(20):
                            print(matris[i][j], end=" ")
                        print()


            elif kategori2 == 2:
                print("Kategori 2 Sağ blok")
                print("Kategori 2 için kalan bilet sayisi :", KategoriKoltukSayisi[1] )
                biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
                satılanBilet = biletAdet
                kategori2SatilanBilet = satılanBilet;
                if biletAdet > 100 or biletAdet <= 0 :
                    print("Kategori 2 için uygun bilet kalmamıştır")
                else:
                    print("Kategori -2 için", biletAdet, "bilet rezerve ediliyor...")
                    time.sleep(1)
                    for i in range(10):
                        for j in range(15,20):
                            if biletAdet > 0:
                                matris[i][j] = "X"
                                biletAdet -= 1

            
                    KategoriKoltukSayisi[1] -= biletAdet
                    print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                    for i in range(10):
                        for j in range(15,20):
                            if matris[i][j] == "X":
                                print(i+1,"-",j+1, end="  ")
                    print()
                    print("Kategori 2 için kalan bilet sayısı:", 100 - satılanBilet)
                    kategoriCiro[1] = satılanBilet * fiyatMatris[1]
                    ciro = kategoriCiro[1]
                    print("Kategori 2 için gelir:",ciro, "TL")

                    print("Salonun durumu:")
                    for i in range(20):
                        for j in range(20):
                            print(matris[i][j], end=" ")
                        print()




        elif kategori == 3:
            print("Kategori 3")
            print("Kategori 3 için kalan bilet sayisi :", KategoriKoltukSayisi[2] )
            biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
            satılanBilet = biletAdet
            kategori3SatilanBilet = satılanBilet;
            if biletAdet > 100 or biletAdet <= 0 :
                print("Kategori 3 için uygun bilet kalmamıştır")
            else:
                print("Kategori -3 için", biletAdet, "bilet rezerve ediliyor...")
                time.sleep(1)
                for i in range(10,20):
                    for j in range(5,15):
                        if biletAdet > 0:
                            matris[i][j] = "X"
                            biletAdet -= 1

            
                KategoriKoltukSayisi[2] -= biletAdet
                print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                for i in range(10,20):
                    for j in range(5,15):
                        if matris[i][j] == "X":
                            print(i+1,"-",j+1, end="  ")
                print()

                print("Kategori 3 için kalan bilet sayısı:", 100 - satılanBilet)
                kategoriCiro[2] = satılanBilet * fiyatMatris[2]
                ciro = kategoriCiro[2]
                print("Kategori 3 için gelir:",ciro, "TL")

                print("Salonun durumu:")
                for i in range(20):
                    for j in range(20):
                        print(matris[i][j], end=" ")
                    print()
        
        elif kategori == 4:
            print("1- Kategori 4 Sol blok")
            print("2- Kategori 4 Sağ blok")
            kategori4 = int(input("Seçiminiz: "))

            if kategori4 == 1:
                print("Kategori 4 Sol blok")
                print("Kategori 4 için kalan bilet sayisi :", KategoriKoltukSayisi[3] )
                biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
                satılanBilet = biletAdet
                kategori4SatilanBilet = satılanBilet;
                if biletAdet > 100 or biletAdet <= 0 :
                    print("Kategori 4 için uygun bilet kalmamıştır")
                else:
                    print("Kategori -4 için", biletAdet, "bilet rezerve ediliyor...")
                    time.sleep(1)
                    for i in range(10,20):
                        for j in range(5):
                            if biletAdet > 0:
                                matris[i][j] = "X"
                                biletAdet -= 1

            
                    KategoriKoltukSayisi[3] -= biletAdet
                    print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                    for i in range(10,20):
                        for j in range(5):
                            if matris[i][j] == "X":
                                print(i+1,"-",j+1, end="  ")
                    print()
                    print("Kategori 4 için kalan bilet sayısı:", 100 - satılanBilet)
                    kategoriCiro[3] = satılanBilet * fiyatMatris[3]
                    ciro = kategoriCiro[3]
                    print("Kategori 4 için gelir:",ciro, "TL")
                    print("Salonun durumu:")
                    for i in range(20):
                        for j in range(20):
                            print(matris[i][j], end=" ")
                        print()
            elif kategori4 == 2:
                print("Kategori 4 Sağ blok")
                print("Kategori 4 için kalan bilet sayisi :", KategoriKoltukSayisi[3] )
                biletAdet = int(input("Kaç bilet almak istiyorsunuz: "))
                satılanBilet = biletAdet
                kategori4SatilanBilet = satılanBilet;
                if biletAdet > 100 or biletAdet <= 0 :
                    print("Kategori 4 için uygun bilet kalmamıştır")
                else:
                    print("Kategori -4 için", biletAdet, "bilet rezerve ediliyor...")
                    time.sleep(1)
                    for i in range(10,20):
                        for j in range(15,20):
                            if biletAdet > 0:
                                matris[i][j] = "X"
                                biletAdet -= 1

            
                    KategoriKoltukSayisi[3] -= biletAdet
                    print("Rezerve edilen koltuklar (Sıra-Koltuk):")
                    for i in range(10,20):
                        for j in range(15,20):
                            if matris[i][j] == "X":
                                print(i+1,"-",j+1, end="  ")
                    print()
                    print("Kategori 4 için kalan bilet sayısı:", 100 - satılanBilet)
                    kategoriCiro[3] = satılanBilet * fiyatMatris[3]
                    ciro = kategoriCiro[3]
                    print("Kategori 4 için gelir:",ciro, "TL")
                    print("Salonun durumu:")
                    for i in range(20):
                        for j in range(20):
                            print(matris[i][j], end=" ")
                        print()

    #salonların durumu 
    elif secim == 2:
        print("Salonun durumu:")
        for i in range(20):
            for j in range(20):
                print(matris[i][j], end=" ")
            print()
    
    #salonların ciro durumu
    elif secim == 3:
        print("Salonların ciro durumu:")
        for i in range(4):
            print(i+1,". kategori ciro durumu:", kategoriCiro[i], "TL")
        
        print()
    
    #salonların doluluk durumu
    elif secim == 4:
        print("Salonların doluluk durumu:")
        print("Kategori 1 doluluk durumu:", 100 - kategori1SatilanBilet, "%" )
        print("Kategori 2 doluluk durumu:", 100 - kategori2SatilanBilet, "%")
        print("Kategori 3 doluluk durumu:", 100 - kategori3SatilanBilet, "%")
        print("Kategori 4 doluluk durumu:", 100 - kategori4SatilanBilet, "%")
        print()


    #her şeyi sıfırla
    elif secim == 5:
        print("Salonlar sıfırlanıyor...")
        time.sleep(1)
        for i in range(20):
            for j in range(20):
                matris[i][j] = "-"
        for i in range(4):
            KategoriKoltukSayisi[i] = 100
            kategoriCiro[i] = 0
        print("Salonlar sıfırlandı.")
        print("Salonun durumu:")
        for i in range(20):
            for j in range(20):
                print(matris[i][j], end=" ")
            print()
        print("Salonların ciro durumu:")
        for i in range(4):
            print(i+1,". kategori ciro durumu:", kategoriCiro[i], "TL")
        print("Salonların doluluk durumu:")
        for i in range(4):
            print(i+1,". kategori doluluk durumu:", 100 - KategoriKoltukSayisi[i], "%")


    #çıkış
    elif secim == 6:
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapıldı.")
        break

