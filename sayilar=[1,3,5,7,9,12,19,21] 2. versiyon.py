sayilar=[1,3,5,7,9,12,19,21]



baslangic=int(input('başlangıç:'))
bitis=int(input('bitiş'))

i= baslangic
while i<bitis:
    i+=1
    if (i%2==1):
      print(i)