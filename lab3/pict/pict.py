from graph import *


from graph import *
from math import sin, cos, pi

def sky(x0, y0, r): #нулевая точка- центр левого нижнего кружка
    x = x0
    y = y0
    for i in range(4):
        penColor("black")
        brushColor("white")
        circle(x, y, 20)
        x += 20
    x = x0 + r//2
    y -= r
    for i in range(3):
        penColor("black")
        brushColor("white")
        circle(x, y, 20)
        x += 20

def tree(x0, y0, r): #нулевая точка - центр основания ствола
    wid = r
    h = 4*r
    brushColor("black")
    rectangle(x0-r//2, y0-h, x0+r//2, y0)

    y = y0 - h - r * 7//2
    penColor("black")
    brushColor("green")
    circle(x0, y, r)

    x = x0 - r
    y += r * 3//2
    for i in range(2):
        penColor("black")
        brushColor("green")
        circle(x, y, r)
        x += 2*r
    y += r//2
    penColor("black")
    brushColor("green")
    circle(x0, y, r)

    x = x0-r
    y += r * 3//2
    for i in range(2):
        penColor("black")
        brushColor("green")
        circle(x, y, r)
        x += 2*r

def home(x0,  y0, side): #нулевая точка - левая верхняя точка дома
    brushColor("brown")
    rectangle(x0, y0, x0 + side, y0 + side)

    brushColor("magenta")
    polygon( [(x0,y0), (x0 + side//2 ,y0 - side * 3//10), (x0+side,y0), (x0,y0)] )

    brushColor("yellow")
    rectangle(x0 + side * 3//10, y0 + side * 4//10, x0 + side * 7//10, y0 + side * 8//10)

def Fone(width, height):
    brushColor("blue")
    rectangle(0, 0, width, height//2)
    brushColor("green")
    rectangle(0, height//2, width, height)
def sun(x0, y0):
    penColor("black")
    brushColor("yellow")
    R = 30
    r = 10
    circle(x0, y0, R)
    n = 8
    alpha = 2*pi/n
    for i in range(n):
        x = x0 + R * cos(alpha*i)
        y = y0 - R * sin(alpha*i)
        circle(x,y, r)

def pair_home_tree(x0,y0, side): #нулевая точка - левый нижний угол дома
    home(x0,y0-side,side)
    tree(x0 + side * 15//10, y0 - side//10, side//5)

Width = 600
Height = 400
windowSize(Width,Height)
canvasSize(Width, Height)

Fone(Width,Height)

sky(Width * 113//145, Height * 20//95, 20)


pair_home_tree(Width * 30//145, Height * 73//95, 150)


sun(Width * 20//145, Height * 20//95)
run()
