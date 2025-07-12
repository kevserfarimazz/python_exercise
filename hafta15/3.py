# Kullanıcının belirlemiş olduğu aralıkta, n adet sayının
#ortalamasını bulan fonksiyonu yazın.

import random

def bul(adet,ilk,son):
    toplam=0
    for i in range(adet):
        sayi=random.randrange(ilk,son)
    
        toplam=toplam+sayi
    sonuc=toplam/adet
    print(sonuc)




bul(90,12,100)
