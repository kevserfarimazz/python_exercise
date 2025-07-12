class musteri:
    def __init__(self,MusID,kadi,email):
        self.MusID=MusID
        self.kadi=kadi
        self.email=email
    def yaz(self):
        print("Müşetri numarası=", self.MusId,"email=",self.email)


class profil(musteri):
    def __init__(self,ad,soyad,sifre,dtarih):
        self.ad=ad
        self.soyad=soyad
        self.sifre=sifre
        self.dtarih=dtarih
    yas=0
    def goster(self):
        self.yas=2024-self.dtarih
        print("Müşterinin yaşı=" self.yas)

class kampanya(musteri):
    def __init__(self,takim,yas,il):
        self.takim=takim
        self.yas=yas
        self.il=il
    def indirim(self):
        if self.takim=="SS":
            self.inoran=90
            print(self.inoran)
        elif self.takim=="GS":
            self.inoran=40
            print(self.inoran)
        else self.takim=="FB":
            self.inoran=30
            print(self.inoran)

class siparis(musteri):
    def __init__(self,u1,u2,u3):
        self.u1=u1
        self.u2=u2
        self.u3=u3
        toplam=0
        u1fiyat=0
        u2fiyat=0
        u3fiyat=0
    def topla(self):
        self.u1fiyat=int(input("birinci ürünün fiyatını giriniz"))
        self.u2fiyat=int(input("ikinci ürünün fiyatını giriniz"))
        self.u3fiyat=int(input("üçüncü ürünün fiyatını giriniz"))
        self.toplam=self.u1fiyat+self.u2fiyat+self.u3fiyat
        print("toplam borç=",self.toplam)
        print("aldğınız ürünler =", self.u1,self.u2,self.u3)

        
Bade=musteri(100,BadeKF,bade@gmail.com)
Bade.yaz()

Bade=profil("Bade","Kevser","1234",1974)
Bade.goster()

Bade=kampanya("SS","Sivas",50)
Bade.indirim()

Bade=siparis("telefon","defter","kalem")
Bade.toplam()