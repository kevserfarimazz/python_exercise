import turtle

ybs=turtle.Turtle()

def harfm(renk):

    ybs.begin_fill()
    ybs.left(90)
    ybs.fd(100)
    ybs.right(135)
    ybs.fd(60)
    ybs.left(90)
    ybs.fd(60)
    ybs.right(135)
    ybs.fd(100)
    ybs.right(90)
    ybs.fd(10)
    ybs.right(90)
    ybs.fd(80)
    ybs.left(135)
    ybs.fd(45)
    ybs.right(90)
    ybs.fd(45)
    ybs.left(135)
    ybs.fd(80)
    ybs.right(90)
    ybs.fd(10)
    ybs.color(renk)
    ybs.end_fill()

harfm("yellow")
ybs.fd(100)
ybs.left(180)
harfu("red")
    
