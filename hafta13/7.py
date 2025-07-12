#Bir manav elma ve armut satmaktadır. elma ve armutub fiyatı her gün
#değişmektedir.  kar oranını da manav belirlemektedir.
# parametrik bir fonksiyon tanımlayarak, bir müşterinin aldığı elma yada
# armut için ödemesi gereken miktarı yazınız.


def elma(kg,fiyat,kar):
    fiyat=kg*fiyat+(((kg*fiyat)/100)*kar)
    print("elma fiyatı:",fiyat)
def armut(kg,fiyat,kar):
    fiyat=kg*fiyat+(((kg*fiyat)/100)*kar)
    print("armut fiyatı=",fiyat)


elma(3,30,10)
armut(5,27,15)
