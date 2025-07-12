import math
class cokgen:
    def __init__(self,kenarsayisi,kenaruzunluk):
        self.kenarsayisi=kenarsayisi
        self.kenaruzunluk=kenaruzunluk
    cevre=0
    alan=0
    def cevre(self):
        self.cevre=self.kenarsayisi*self.kenaruzunluk
        print("Çokgenin çevresi=", self.cevre)
    def alan(self):
        self.alan=


ilk=cokgen(12,8)
ilk.cevre()