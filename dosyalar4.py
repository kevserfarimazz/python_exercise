class urun:
    ad=""
    kod=""
    kategori=""
    alisfiyat=0
    karoran=0
    stok=0
    kdv=0
    indirim=0
    sonfiyat=0
    def hesap(self):
        if self.stok>0:
            self.sonfiyat=self.alisfiyat+(self.alisfiyat*self.karoran/100) + (self.alisfiyat*self.kdv/100)
            print("ürünün satış fiyatı",self.sonfiyat)

gomlek=urun()
gomlek.ad="polo yaka gömlek"
gomlek.kategori="giysi"
gomlek.kod="12423"
gomlek.stok=100
gomlek.alisfiyat=200
gomlek.karoran=60
gomlek.kdv=20
gomlek.hesap()
