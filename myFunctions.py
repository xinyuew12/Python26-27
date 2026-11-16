import turtle
bob=turtle.Turtle()

def star(size,c):
    bob.color(c)
    bob.fillcolor(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(size)
        bob.right(144)
    bob.end_fill()

def polygon(sides,dist,c):
    angle=360/sides
    bob.color(c)
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def fill_moon(x,y):
    jump(x,y)
    circle(50,"white")

def moon(x,y):
    jump(x,y)
    circle(50,"white")
    jump(x,y+5)
    circle(45,"black")

def moon1(x,y):
    jump(x,y)
    circle(50,"white")
    jump(x+25,y)
    circle(45,"black")

def moon2(x,y):
    jump(x,y)
    circle(50,"white")
    jump(x+10,y)
    circle(45,"black")

def circle(size,c):
    bob.fillcolor(c)
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    



