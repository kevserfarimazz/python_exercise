sayilar=[1,3,5,7,9,12,19,21]

for sayi in sayilar:
    if(sayi%3==0):
      print(sayi)

toplam=0
for sayi in sayilar:
   toplam+= sayi
   print('toplam',toplam)

for sayi in sayilar:
   if(sayi%2==1):
      print(sayi**2)

sehirler=['sivas','malatya','kayseri','trabzon','istanbul']
for sehir in sehirler:
   if (len(sehir)<=5):
      print(sehir)   


urunler= [
   {'name':'samsungs6','price':'3000'},
   {'name':'samsungs7','price':'5000'},
   {'name':'samsungs8','price':'6000'},
   {'name':'samsungs9','price':'7000'}
]
toplam=0
for urun in urunler:
   fiyat=int(urun['price'])
   toplam+=fiyat
print(toplam)

for urun in urunler:
   if(int(urun['price'])<=5000):
      print(urun['name'])