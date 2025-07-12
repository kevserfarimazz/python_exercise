# Sahneye x adet, 5 farklı renkte ,kullanıcının belirleyece
#ği büyüklükte farklı koordinatlarda kareler çizen
# parametrik bir fonksiyon tanımlayınız.


import turtle
import random
ybs=turtle.Turtle()

def kare(sayi,ksay,bsay):
    for i in range(sayi):
        deger=random.randrange(ksay,bsay)
        print(deger)

kare(40,100,400)
        
        
