from ogrenciprojesi import *



print("""
Öğrenci İşlerine hoşgeldiniz.....

***********************************************
                                              *
1- Öğrencileri Göster                         *
                                              *
2- Öğrenci Sorgula                            * 
                                              *
3- Öğrenci Ekle                               *
                                              *
4- Öğrenci Sil                                *
                                              * 
5- Bölüm değiştir                             * 
                                              *
6- Sene Uzatma                                *
                                              *
7- Ortalama değiştirme                        *  
                                              *
Çıkış yapmak için 'q' ya basınız...           * 
                                              *
***********************************************                                   
""")

ogrenciprojesi = Sınıf()


while True:

    islem = input("Lütfen yapmak istediğiniz işlemi giriniz: ")

    if islem == "q":
        print("Programdan çıkılıyor....")

        print("Programdan çıkıldı......")

        break

    elif islem == "1":

        print("Öğrencilerin bilgileri....")

        time.sleep(2)

        ogrenciprojesi.öğrencileri_göster()

    elif islem == "2":

        tc = int(input("Lütfen öğrencinin TC sini giriniz: "))

        print("Öğrenci sorgulanıyor....")

        time.sleep(2)

        ogrenciprojesi.öğrenci_sorgula(tc)

    elif islem == "3":

        tc = int(input("TC: "))
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        yas = int(input("Yaş: "))
        bölüm = input("Bölüm: ")
        ortalama = float(input("Ortalama: "))
        sene = int(input("Bölümünüz kaç sene: "))

        ogrenci = Öğrenciler(tc,isim,soyisim,yas,bölüm,ortalama,sene)
        print("Öğrenci ekleniyor....")
        time.sleep(2)
        ogrenciprojesi.öğrenci_ekle(ogrenci)
        print("Öğrenci eklendi....")

    elif islem == "4":

        tc = int(input("Lütfen silmek istediğiniz öğrencinin TC sini giriniz: "))

        cevap = input("Emin misiniz? E/H")
        if cevap == "E":
            print("Öğrenci siliniyor....")
            time.sleep(2)

            ogrenciprojesi.öğrenci_sil(tc)
            print("Öğrenci silindi....")

    elif islem == "5":

        tc = int(input("Lütfen bölümünü değiştirmek istediğiniz öğrencinin TC sini giriniz: "))
        time.sleep(2)
        print("Bölüm değiştiriliyor....")

        ogrenciprojesi.bölüm_değiştir(tc)

        print("Bölüm değiştirildi....")

    elif islem == "6" :
        tc = int(input("Lütfen senesini uzatmak istediğiniz öğrencinin TC sini giriniz: "))

        print("Sene mi uzadı, hayırlısı olsun kardeşim, bir sene daha bizlesin :)) ")
        time.sleep(2)

        ogrenciprojesi.sene_uzama(tc)
        print("Sene uzatıldı....")

    elif islem == "7":
        tc = int(input("Lütfen ortalamasını değiştirmek istediğiniz öğrencinin TC sini giriniz: "))


        ogrenciprojesi.ortalama_değiştirme(tc)
        print("Ortalama değiştiriliyor....")
        time.sleep(2)
        print("Ortalama değiştirildi....")




    else :
        print("Lütfen geçerli bir işlem giriniz....")





