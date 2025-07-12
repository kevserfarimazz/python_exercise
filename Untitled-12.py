
import random

sayi=random.randint(1,10)
hak=5
sayac=0

while hak>0:
     hak-=1
     sayac+=1
     tahmin=int(input('tahmin:'))

     if sayi==tahmin:
        print('tebrikler {sayac}. defada bildiniz. toplam puanınıoz {100-(20)*(sayac-1)}')
        break
     elif sayi>tahmin:
         print('yukarı')
     else:
        print('aşağı')

     if hak==0:
        print(f'hakkınız bitti. tutulan sayı:{sayi}')
        
    #SAYACIM NEDEN ÇALIŞMIYOR????
