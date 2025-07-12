class calisan:
    yas=0
    meslek=""
    kidem=0
    pozisyon=""
    cocuksay=0
    basucret=0
    sonmaas=0
    prom=0
    def maas(self):
        self.sonmaas=self.basucret + (1000*self.cocuksay)
        print(self.sonmaas)
    def promosyon(self):
        self.prom=self.kidem*500
        print("Promosyon Tutarı",self.prom)

Kevser=calisan()
Kevser.yas=25
Kevser.meslek="yönetici"
Kevser.cocuksay=1
Kevser.basucret=32000
Kevser.kidem=7
Kevser.maas()
Kevser.promosyon()
