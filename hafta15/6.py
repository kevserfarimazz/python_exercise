#Bir öğrencinin ARasınav ödev, ve final notlarını fonksiyon
# olarak tanımlayıp ortalamasınu bulun. ara sın %30
# ödev %20 , final % 50 etkili. Fonksiyon öğrencinin
# ortalaması ile birlikte dersten geçme kalma durumunuda
# hesaplayacak 60 üzeri geçer, 60 altı kalır.

def hesap(vize,odev,final):
    ortalama=(vize*0.3)+(odev*0.2)+(final*0.5)
    if ortalama>=60:
        print("ortalamanız=", ortalama,"Geçtiniz")
    if ortalama<60:
        print("ortalamanız=", ortalama,"Kaldınız")

hesap(60,40,90)   
hesap(30,70,40)
hesap(70,80,50)
