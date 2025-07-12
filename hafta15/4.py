# Kullanıcının belirlemiş olduğu aralıkta, n adet sayının
#ortalamasını bulan fonksiyonu yazın.

import random

def bul(adet):
    toplam=0
    ilk=int(input("başlangıç sayi giriniz"))
    son=int(input("son sayıyı giriniz"))
    for i in range(adet):
        sayi=random.randrange(ilk,son)
    
        toplam=toplam+sayi
    sonuc=toplam/adet
    print(sonuc)




bul(90)
