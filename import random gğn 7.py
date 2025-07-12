import random 

sayi=random.randint(1,10)
hak=5

while hak>0:
    hak-=1
    tahmin = int(input('tahmin:' ))

    if sayi==tahmin:
        print('tebrikler bildiniz.')
        break 
    elif sayi>tahmin:
        print('yukarı')
    else:
        print('aşağı')
        
    if hak==0:
        print('hakkınız bitti.tutulan sayı: {sayi}')