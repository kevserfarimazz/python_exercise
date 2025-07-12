import turtle
import random

ybs=turtle.Turtle()
ybs.speed(0)


for i in range(100):
    renk=random.randrange(1,6)
    if renk==1:
        ybs.pencolor("blue")
    elif renk==2:
        ybs.pencolor("red")
    elif renk==3:
        ybs.pencolor("yellow")
    elif renk==4:
        ybs.pencolor("green")
    elif renk==5:
        ybs.pencolor("pink")
    
    ybs.circle(10+(i*2))
    print(10+(i*2))





    







    
