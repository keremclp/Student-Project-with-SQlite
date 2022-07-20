import sqlite3
import time



class Öğrenciler():
    def __init__(self,TC,isim, soyisim, yaş, bölüm, ortalama, sene):
        self.TC = TC
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
        self.bölüm = bölüm
        self.ortalama = ortalama
        self.sene = sene

    def __str__(self):
        return "TC : {}\nİsim : {}\nSoyisim : {}\nYaş : {}\nBölüm : {}\nOrtalama: {}\nKaç yıl : {} ".format(self.TC,self.isim,self.soyisim,self.yaş,self.bölüm,self.ortalama,self.sene)


class Sınıf() :

    def __init__(self):

        self.baglantı_olustur()

    def baglantı_olustur(self):

        self.bağlantı = sqlite3.connect("Öğrenci Verileri.db")

        self.cursor = self.bağlantı.cursor()

        sorgu = "Create table if not exists Öğrenciler(TC INT,isim TEXT, soyisim TEXT, yaş INT, bölüm TEXT, ortalama INT, sene INT)"

        self.cursor.execute(sorgu)

        self.bağlantı.commit()

    def bağlantı_kes(self):

        self.bağlantı.close()


    def öğrencileri_göster(self):

        sorgu = "Select * From Öğrenciler"

        self.cursor.execute(sorgu)

        data = self.cursor.fetchall()

        if len(data) == 0 :
            print("Sınıfta öğrenci bulunmamaktadır....")

        else:
            for i in data :
                öğrenci = Öğrenciler(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
                print(öğrenci)

    def öğrenci_sorgula(self,TC):

        sorgu = "Select * From Öğrenciler where TC = ?"

        self.cursor.execute(sorgu,(TC,))

        data = self.cursor.fetchall()

        for i in data :
            öğrenci = Öğrenciler(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4],data[0][5],data[0][6])

            print(öğrenci)


    def öğrenci_ekle(self,insan):

        sorgu = "Insert Into Öğrenciler Values(?,?,?,?,?,?,?)"

        self.cursor.execute(sorgu,(insan.TC,insan.isim,insan.soyisim,insan.yaş,insan.bölüm,insan.ortalama,insan.sene))

        self.bağlantı.commit()


    def öğrenci_sil(self,TC):

        sorgu = "Delete From Öğrenciler where TC = ?"

        self.cursor.execute(sorgu,(TC,))

        self.bağlantı.commit()


    def bölüm_değiştir(self,TC):

        sorgu = "Select * From Öğrenciler where TC = ?"

        self.cursor.execute(sorgu,(TC,))

        data = self.cursor.fetchall()

        if len(data)==0:
            print("Sınıfta öğrenci bulunmamaktadır....")

        else:
            bölüm = data[0][4]

            yeni_bölüm = input("Lütfen yeni bölümü giriniz: ")

            bölüm = yeni_bölüm

            sorgu2 = "Update Öğrenciler set bölüm = ? where TC = ?"

            self.cursor.execute(sorgu2,(bölüm,TC,))

            self.bağlantı.commit()

            print("Bölüm değiştirildi....")


    def sene_uzama(self,TC):

        sorgu = "Select * From Öğrenciler where TC = ?"

        self.cursor.execute(sorgu,(TC,))

        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Sınıfta öğrenci bulunmamaktadır....")

        else:
            sene = data[0][6]

            sene+=1

            sorgu2 = "Update Öğrenciler set sene=? where TC=?"

            self.cursor.execute(sorgu2,(sene,TC,))

            self.bağlantı.commit()

    def ortalama_değiştirme(self,TC):

        sorgu = "Select * From Öğrenciler where TC = ?"

        self.cursor.execute(sorgu,(TC,))

        data = self.cursor.fetchall()

        if len(data)==0:
            print("Sınıfta öğrenci bulunmamaktadır.....")

        else:
            ortalama = data[0][5]

            cevap = input("Artırmak için 'artır' yazın... "
                          "Azaltmak için 'azalt' yazın... "
                          "Cevap:  ")

            if cevap == "artır":

                cevap2 = float(input("Ne kadar artırmak istiyorsunuz: "))

                ortalama += cevap2
            elif cevap == "azalt":
                cevap2 = float(input("Ne kadar artırmak istiyorsunuz: "))

                ortalama -= cevap2
            else:
                print("Lütfen geçerli bir işlem giriniz.....")


        sorgu2 = "Update Öğrenciler set ortalama=? where TC=?"

        self.cursor.execute(sorgu2,(ortalama,TC,))

        self.bağlantı.commit()




















