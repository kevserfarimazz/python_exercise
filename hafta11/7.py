import turtle
import random
ybs=turtle.Turtle()
ybs.speed(10)

for i in range(50):

    xdeg=random.randrange(-200,200)
    ydeg=random.randrange(-200,200)
    buy=random.randrange(10,80)
    
    print(xdeg,ydeg,buy)
    ybs.pu()
    ybs.goto(xdeg,ydeg)
    ybs.pd()
    ybs.circle(buy)







    
