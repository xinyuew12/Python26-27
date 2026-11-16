from myFunctions import*
from random import*
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor("black")

fill_moon(0, 0)
moon1(-120, 75)
moon2(-260, 120)
moon(-400, 90)
fill_moon(-480, 0)
moon1(-400, -90)
moon2(-260, -120)
moon(-120, -75)

fill_moon(120, 75)
moon1(260, 120)
moon2(400, 90)
moon(480, 0)
fill_moon(400, -90)
moon1(260, -120)
moon2(120, -75)

for times in range(10):
    jump(0,400)
    bob.color("lightyellow")
    bob.circle(times*100)
    bob.setheading(180)

for times in range(100):
    x=randint(-500,500)
    y=randint(-500,500)
    size=randint(5,10)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    c=(r,g,b)
    jump(x,y)
    star(size,c)
  
for times in range(100):
    x=randint(-500,500)
    y=randint(-500,500)
    side=randint(3,8)
    dist=randint(1,10)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    c=(r,g,b)
    jump(x,y)
    polygon(side,dist,c)
