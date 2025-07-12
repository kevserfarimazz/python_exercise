bos=[]
toplam=0

adet=int(input("ka. adet girerek işlem yapacaksınız?"))

for i in range(adet):
    sayi=int(input("sayi giriniz"))
    bos=bos+[sayi]
    print(bos)
    toplam=toplam+sayi
print("listedeki sayıların ortalaası=",toplam/adet)
