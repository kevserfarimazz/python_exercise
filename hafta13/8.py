import turtle

ybs=turtle.Turtle()

#ybs.circle(30)

def daire (cap):
    for i in range(360):
        ybs.fd(cap/10)
        ybs.left(1)
        ybs.speed(0)

daire(20)
daire(15)

