import turtle

ybs=turtle.Turtle()

def kare(buyuk):

    for i in range(4):
        ybs.fd(buyuk)
        ybs.left(90)

for i in range(50):
    kare(i*5)


