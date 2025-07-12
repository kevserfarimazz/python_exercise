# Sahneye x adet, 5 farklı renkte ,kullanıcının belirleyece
#ği büyüklükte farklı koordinatlarda kareler çizen
# parametrik bir fonksiyon tanımlayınız.


import turtle
import random
ybs=turtle.Turtle()
ybs.speed(0)
def kare(sayi,ksay,bsay):
    for i in range(sayi):
        deger=random.randrange(ksay,bsay)
        renk=random.randrange(1,6)
        print("renk=",renk)
        xkor=random.randrange(-350,350)
        ykor=random.randrange(-350,350)
        ybs.penup()
        ybs.goto(xkor,ykor)
        ybs.pendown()
        if renk==1:
            ybs.begin_fill()
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.color("blue")
            ybs.end_fill()
        elif renk==2:
            ybs.begin_fill()
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.color("yellow")
            ybs.end_fill()
        elif renk==3:
            ybs.begin_fill()
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.color("red")
            ybs.end_fill()
        elif renk==4:
            ybs.begin_fill()
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.color("pink")
            ybs.end_fill()
        elif renk==5:
            ybs.begin_fill()
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.fd(deger)
            ybs.left(90)
            ybs.color("gray")
            ybs.end_fill()
        print(deger)
        

kare(50,30,150)
        
        
