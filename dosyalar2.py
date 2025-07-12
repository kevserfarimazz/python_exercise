sayilar=[3,23,45,67,54,60,4,3,78]
sayiiki=[34,56,54,76,32,54,2,3,2]

def bul(liste,sayi):
    adet=0
    for i in liste:

        if i==sayi:
            adet=adet+1
    print(sayi,"dan",adet,"kadar vardır")

bul(sayilar,4)


##dizide kaç tame fonksiyondanvar