from graph import *


brushColor("blue")
rectangle(0, 0, 500, 200)

brushColor("green")
rectangle(0, 200, 500, 400)


brushColor("brown")
rectangle(120, 180, 220, 280)


brushColor("magenta")
polygon( [(120,180), (170,150), (220,180), (120,180)] )

brushColor("yellow")
rectangle(150, 220, 190, 260)

brushColor("black")
rectangle(330, 190, 350, 270)


x = 250
for i in range(4):
    penColor("black")
    brushColor("white")
    circle(x, 60, 20)
    x += 20

x = 260
for i in range(3):
    penColor("black")
    brushColor("white")
    circle(x, 40, 20)
    x += 20

penColor("black")
brushColor("green")
circle(340, 120, 20)

x = 320
for i in range(2):
    penColor("black")
    brushColor("green")
    circle(x, 150, 20)
    x += 40

penColor("black")
brushColor("green")
circle(340, 160, 20)

x = 320
for i in range(2):
    penColor("black")
    brushColor("green")
    circle(x, 190, 20)
    x += 40

run()
