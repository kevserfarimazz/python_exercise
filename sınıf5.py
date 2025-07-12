class kisi:
    def __init__(self,ad,yas):
        self.ad=ad
        self.yas=yas
    def kunye(self):
        print("yeni nesnenin adı=",self.ad)
        print("yeni nesnenin yaşı",self.yas)
        
personel1=kisi("Kevser",23)
personel1.kunye()

per2=kisi("Elif",24)
per2.kunye()

#Nesne özelliklerini değiştirme

per2.ad="Dilara"
per2.kunye()

#Nesne özellikleini silme-- mesela per1 nesnesinin yaşını silelim.
 