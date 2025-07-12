sayilar=[1,2,3,4,5,6,7,8,9]

adet=0
toplam=0
for i in sayilar:
    print("listedeki sayı=",i)
    adet=adet+1
    print("şu anki sayı adeti=",adet)
    toplam=toplam+i
    print("ara toplam=",toplam)

print("listedeki sayı adedi=",adet)
print=("listedeki sayıların toplamı=",toplam)
print("listedeki sayıların ortalaması=",toplam/adet)