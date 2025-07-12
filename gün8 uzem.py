# toplpamsayi=0
# for i in range(1,100):
#     if i%7==0 or i%11==0:
#         print(i)
#         toplpamsayi=toplpamsayi+i
#         print("şu ana kadar nulunan sayı",toplpamsayi)

# ##  

# def yap(ilk,son,art):
#     for i in range(ilk,son,art):
#         print(i)
# yap(5,20,2)
# yap(10,1000,58)

# ##

# import random
# sayitahmin=0
# for i in range(0,100):          bu kısmı ben denedim doğru değil ama 
#    if  tahminhakkı<=5:
#        break
   
##
# import random

# sayi=random.randrange(1,10)
# print(sayi)

# for i in range(5):
#     tahmin=(int(input("bilgisayarın tuttğu sayıyı tahmin et")))
#     if tahmin==sayi:
#         print("tebrikler bildiniz",tahmin)
#         break
#     elif tahmin>sayi:
#         print("aşağı")
#     elif tahmin<sayi:
#         print("yukarı")

##


import random

for i in range(10):
    sayi=random.randrange(1,1000)
    if sayi%2==0:
        print(sayi)


##