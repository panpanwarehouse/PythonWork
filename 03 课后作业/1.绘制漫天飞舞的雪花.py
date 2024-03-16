import turtle
import random
def getcolor():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)
def getsize():
    color=random.randint(20,70)
    return color
def getposition():
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    return (x,y)
    # 设置屏幕背景色和填充颜色
    screen = turtle.Screen()
turtle.bgcolor("black")
    # 创建雪花对象
snowflakes = []
for i in range(200):
    t=turtle
    snowflakes.append(t)
    # 随机设置雪花的位置、大小和颜色
def kouch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            kouch(size/3,n-1)

def Create(turtle):
    color=getcolor()
    size=getsize()
    startposition=getposition()
    turtle.pencolor(color)
    turtle.setup(600,600)
    turtle.speed(100)
    turtle.penup()
    turtle.goto(startposition[0],startposition[1])
    turtle.pendown()
    turtle.pensize(2)
    level=3
    kouch(size,level)
    turtle.right(120)
    kouch(size,level)
    turtle.right(120)
    kouch(size,level)
    turtle.hideturtle()
    #turtle.done()
for i in snowflakes:
    Create(i)
