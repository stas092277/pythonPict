from graph import *
from math import cos, sin, pi


# ---------------ПАРЕНЬ-------------------
def menL(Width, Height, x_point_touch, y_point_touch, R_head, color_head, x_bias):
    foot_size = Width // 16

    # рисуем тело
    a = Width // 12  # Х-радиус
    b = Height // 6  # Y-радиус
    x0_body = Width // 4 + a + x_bias
    y0_body = Height // 2
    ellips(x0_body, y0_body, a, b, "gray")

    # рисуем голову
    x0_head = x0_body
    y0_head = y0_body - b - R_head + 5
    penColor(color_head)
    brushColor(color_head)
    circle(x0_head, y0_head, R_head)

    # рисуем ноги
    penColor("black")
    leg_long = Height // 4
    x_left_leg_start = x0_body - a // 2 
    y_left_leg_start = y0_body + b * 7 // 8
    x_left_leg_finish = x_left_leg_start - round(cos(pi / 2 * 3 / 4) * leg_long)
    y_left_leg_finish = y_left_leg_start + round(sin(pi / 2 * 3 / 4) * leg_long)
    line(x_left_leg_start, y_left_leg_start,
         x_left_leg_finish, y_left_leg_finish)
    x_left_foot_start = x_left_leg_finish 
    y_left_foot_start = y_left_leg_finish
    x_left_foot_finish = x_left_foot_start - foot_size 
    y_left_foot_finish = y_left_foot_start
    line(x_left_foot_start, y_left_foot_start,
         x_left_foot_finish, y_left_foot_finish)

    x_right_leg_start = x0_body + a // 2 
    y_right_leg_start = y0_body + b * 7 // 8 - 2
    x_right_leg_finish = x_right_leg_start + round(cos(pi / 2 * 99 / 100) * leg_long) 
    y_right_leg_finish = y_right_leg_start + round(sin(pi / 2 * 99 / 100) * leg_long)
    line(x_right_leg_start, y_right_leg_start,
         x_right_leg_finish, y_right_leg_finish)
    x_right_foot_start = x_right_leg_finish
    y_right_foot_start = y_right_leg_finish
    x_right_foot_finish = x_right_foot_start + foot_size 
    y_right_foot_finish = y_right_foot_start
    line(x_right_foot_start, y_right_foot_start,
         x_right_foot_finish, y_right_foot_finish)

    # рисуем руки
    x_right_hand_start = x0_body + a // 2 
    y_right_hand_start = y0_body - b * 7 // 8
    x_right_hand_finish = x_point_touch 
    y_right_hand_finish = y_point_touch
    line(x_right_hand_start, y_right_hand_start,
         x_right_hand_finish, y_right_hand_finish)

    x_left_hand_start = x0_body - a // 2 
    y_left_hand_start = y0_body - b * 7 // 8
    x_left_hand_finish = x0_body - 2 * a 
    y_left_hand_finish = Height * 9 // 16
    line(x_left_hand_start, y_left_hand_start,
         x_left_hand_finish, y_left_hand_finish)


def menR(Width, Height, x_point_touch, y_point_touch, R_head, color_head, x_bias):
    foot_size = Width // 16

    # рисуем тело
    a = Width // 12  # Х-радиус
    b = Height // 6  # Y-радиус
    x0_body = Width // 4 + a + x_bias
    y0_body = Height // 2
    ellips(x0_body, y0_body, a, b, "gray")

    # рисуем голову
    x0_head = x0_body
    y0_head = y0_body - b - R_head + 5
    penColor(color_head)
    brushColor(color_head)
    circle(x0_head, y0_head, R_head)

    # рисуем ноги
    penColor("black")
    leg_long = Height // 4
    x_left_leg_start = x0_body - a // 2 
    y_left_leg_start = y0_body + b * 7 // 8
    x_left_leg_finish = x_left_leg_start - round(cos(pi / 2 * 3 / 4) * leg_long)
    y_left_leg_finish = y_left_leg_start + round(sin(pi / 2 * 3 / 4) * leg_long)
    line(x_left_leg_start, y_left_leg_start,
         x_left_leg_finish, y_left_leg_finish)
    x_left_foot_start = x_left_leg_finish 
    y_left_foot_start = y_left_leg_finish
    x_left_foot_finish = x_left_foot_start - foot_size 
    y_left_foot_finish = y_left_foot_start
    line(x_left_foot_start, y_left_foot_start,
         x_left_foot_finish, y_left_foot_finish)

    x_right_leg_start = x0_body + a // 2 
    y_right_leg_start = y0_body + b * 7 // 8 - 2
    x_right_leg_finish = x_right_leg_start + round(cos(pi / 2 * 99 / 100) * leg_long) 
    y_right_leg_finish = y_right_leg_start + round(sin(pi / 2 * 99 / 100) * leg_long)
    line(x_right_leg_start, y_right_leg_start,
         x_right_leg_finish, y_right_leg_finish)
    x_right_foot_start = x_right_leg_finish
    y_right_foot_start = y_right_leg_finish
    x_right_foot_finish = x_right_foot_start + foot_size 
    y_right_foot_finish = y_right_foot_start
    line(x_right_foot_start, y_right_foot_start,
         x_right_foot_finish, y_right_foot_finish)

    # рисуем руки
    x_right_hand_start = x0_body - a // 2 
    y_right_hand_start = y0_body - b * 7 // 8
    x_right_hand_finish = x_point_touch 
    y_right_hand_finish = y_point_touch
    line(x_right_hand_start, y_right_hand_start,
         x_right_hand_finish, y_right_hand_finish)

    x_left_hand_start = x0_body + a // 2 
    y_left_hand_start = y0_body - b * 7 // 8
    x_left_hand_finish = x0_body + 2 * a 
    y_left_hand_finish = Height * 9 // 16
    line(x_left_hand_start, y_left_hand_start,
         x_left_hand_finish, y_left_hand_finish)    



def girlL(Width, Height, x_point_touch, y_point_touch, R_head, color_head, x_bias):
    # рисуем тело
    x0_body = Width * 11 / 16 + x_bias
    y0_body = Height // 2
    h = Height // 3
    wid_down = h * 7 // 10
    x1_triag = x0_body - wid_down // 2
    y1_triag = y0_body + h // 2
    x2_triag = x0_body + wid_down // 2
    y2_triag = y0_body + h // 2
    x3_triag = x0_body
    y3_triag = y0_body - h // 2
    penColor(252, 116, 253)
    brushColor(252, 116, 253)
    polygon([(x1_triag, y1_triag),
             (x2_triag, y2_triag),
             (x3_triag, y3_triag),
             (x1_triag, y1_triag)])

    # рисуем ноги
    x_left_leg_1 = x_left_leg_2 = x0_body - wid_down // 6
    x_right_leg_1 = x_right_leg_2 = x0_body + wid_down // 6
    y_left_leg_1 = y_right_leg_1 = y0_body + h // 2
    y_left_leg_2 = y_right_leg_2 = y_left_leg_3 = y_right_leg_3 = \
        y0_body + h // 2 + wid_down * 5 // 7
    x_left_leg_3 = x_left_leg_2 - wid_down // 7
    x_right_leg_3 = x_right_leg_2 + wid_down // 7
    penColor("black")
    polyline([(x_left_leg_1, y_left_leg_1),
              (x_left_leg_2, y_left_leg_2),
              (x_left_leg_3, y_left_leg_3)])
    polyline([(x_right_leg_1, y_right_leg_1),
              (x_right_leg_2, y_right_leg_2),
              (x_right_leg_3, y_right_leg_3)])

    # рисуем голову
    penColor(color_head)
    brushColor(color_head)
    x0_head = x0_body
    y0_head = y0_body - h // 2 - R_head + 5
    circle(x0_head, y0_head, R_head)

    # рисуем руки
    penColor("black")
    brushColor("black")
    x1_left_hand_1 = x0_body - wid_down * 3 // 35
    y1_left_hand_1 = y0_body - h * 2 // 5
    x2_left_hand_2 = x_point_touch
    y2_left_hand_2 = y_point_touch
    line(x1_left_hand_1, y1_left_hand_1,
         x2_left_hand_2, y2_left_hand_2)

    x1_right_hand_1 = x0_body + wid_down * 3 // 35 - 2
    y1_right_hand_1 = y0_body - h * 2 // 5
    step = h // 3  # длина плеча и предплечья
    x2_right_hand_2 = x1_right_hand_1 + step * sin(pi / 2 * 30 / 90)
    y2_right_hand_2 = y1_right_hand_1 + step * cos(pi / 2 * 30 / 90)
    x3_right_hand_3 = x2_right_hand_2 + step * cos(pi / 2 * 30 / 90)
    y3_right_hand_3 = y2_right_hand_2 - step * sin(pi / 2 * 30 / 90)
    polyline([(x1_right_hand_1, y1_right_hand_1),
              (x2_right_hand_2, y2_right_hand_2),
              (x3_right_hand_3, y3_right_hand_3)])


def girlR(Width, Height, x_point_touch, y_point_touch, R_head, color_head, x_bias):
    # рисуем тело
    x0_body = Width * 11 / 16 + x_bias
    y0_body = Height // 2
    h = Height // 3
    wid_down = h * 7 // 10
    x1_triag = x0_body - wid_down // 2
    y1_triag = y0_body + h // 2
    x2_triag = x0_body + wid_down // 2
    y2_triag = y0_body + h // 2
    x3_triag = x0_body
    y3_triag = y0_body - h // 2
    penColor(252, 116, 253)
    brushColor(252, 116, 253)
    polygon([(x1_triag, y1_triag),
             (x2_triag, y2_triag),
             (x3_triag, y3_triag),
             (x1_triag, y1_triag)])

    # рисуем ноги
    x_left_leg_1 = x_left_leg_2 = x0_body - wid_down // 6
    x_right_leg_1 = x_right_leg_2 = x0_body + wid_down // 6
    y_left_leg_1 = y_right_leg_1 = y0_body + h // 2
    y_left_leg_2 = y_right_leg_2 = y_left_leg_3 = y_right_leg_3 = \
        y0_body + h // 2 + wid_down * 5 // 7
    x_left_leg_3 = x_left_leg_2 - wid_down // 7
    x_right_leg_3 = x_right_leg_2 + wid_down // 7
    penColor("black")
    polyline([(x_left_leg_1, y_left_leg_1),
              (x_left_leg_2, y_left_leg_2),
              (x_left_leg_3, y_left_leg_3)])
    polyline([(x_right_leg_1, y_right_leg_1),
              (x_right_leg_2, y_right_leg_2),
              (x_right_leg_3, y_right_leg_3)])

    # рисуем голову
    penColor(color_head)
    brushColor(color_head)
    x0_head = x0_body
    y0_head = y0_body - h // 2 - R_head + 5
    circle(x0_head, y0_head, R_head)

    # рисуем руки
    penColor("black")
    brushColor("black")
    x1_left_hand_1 = x0_body + wid_down * 3 // 35
    y1_left_hand_1 = y0_body - h * 2 // 5
    x2_left_hand_2 = x_point_touch
    y2_left_hand_2 = y_point_touch
    line(x1_left_hand_1, y1_left_hand_1,
         x2_left_hand_2, y2_left_hand_2)

    x1_right_hand_1 = x0_body - wid_down * 3 // 35 
    y1_right_hand_1 = y0_body - h * 2 // 5
    step = h // 3  # длина плеча и предплечья
    x2_right_hand_2 = x1_right_hand_1 - step * sin(pi / 2 * 30 / 90)
    y2_right_hand_2 = y1_right_hand_1 + step * cos(pi / 2 * 30 / 90)
    x3_right_hand_3 = x2_right_hand_2 - step * cos(pi / 2 * 30 / 90)
    y3_right_hand_3 = y2_right_hand_2 - step * sin(pi / 2 * 30 / 90)
    polyline([(x1_right_hand_1, y1_right_hand_1),
              (x2_right_hand_2, y2_right_hand_2),
              (x3_right_hand_3, y3_right_hand_3)])




#нарисовать эллипс
def in_ellips(x,y, x0, y0, a, b)  :
    if ( (x-x0)**2/(a**2) + (y-y0)**2/(b**2) <= 1):
        return True
    else :
        return False
def ellips(x0, y0, a, b, color):
    for x in range(x0-a,x0+a):
        for  y in range(y0-b,y0+b):
            if in_ellips(x,y, x0, y0, a, b):
                point(x,y,color)

def iceCream(Width, Height, x_point_touch, y_point_touch):
    side = Height // 8
    r = side // 4
    x1_triangle = x_point_touch   
    y1_triangle = y_point_touch
    x2_triangle = x1_triangle - side * cos(pi / 2 * 29 / 90) 
    y2_triangle = y1_triangle - side * sin(pi / 2 * 29 / 90)
    x3_triangle = x2_triangle + side * cos(pi / 2 * (60 - 29) / 90)
    y3_triangle = y2_triangle - side * sin(pi / 2 * (60 - 29) / 90)
    penColor("yellow")
    brushColor("yellow")
    polygon([(x1_triangle, y1_triangle),
             (x2_triangle, y2_triangle),
             (x3_triangle, y3_triangle),
             (x1_triangle, y1_triangle)])

    x1_circ = x2_triangle + (x3_triangle - x2_triangle - 4) // 4
    y1_circ = y2_triangle - r
    x2_circ = x2_triangle + (x3_triangle - x2_triangle - 4) * 3 // 4
    y2_circ = y1_circ - 2 * r * sin(pi / 2 * (60 - 29) / 90)
    x3_circ = x1_circ + r // 4 
    y3_circ = y1_circ - 2 * r * 3 // 4
    penColor("purple")
    brushColor("purple")
    circle(x1_circ, y1_circ, r)
    penColor("red")
    brushColor("red")
    circle(x2_circ, y2_circ, r)
    penColor("white")
    brushColor("white")
    circle(x3_circ, y3_circ, r)

def ball(Width, Height, x_point_touch, y_point_touch):
    h = Height // 3
    x1_stick = x_point_touch - 5
    y1_stick = y_point_touch + 10
    stick_len = h // 2
    alpha = 80
    x2_stick = x1_stick + stick_len * cos(pi / 2 * alpha / 90)
    y2_stick = y1_stick - stick_len * sin(pi / 2 * alpha / 90)
    penColor("black")
    line(x1_stick, y1_stick, x2_stick, y2_stick)

    triag_side = h // 3
    x1_triag = x2_stick
    y1_triag = y2_stick
    betta = alpha - 30
    x2_triag = x1_triag + triag_side * cos(pi / 2 * betta / 90)
    y2_triag = y1_triag - triag_side * sin(pi / 2 * betta / 90)
    gamma = 60 - betta
    x3_triag = x2_triag - triag_side * cos(pi / 2 * gamma / 90)
    y3_triag = y2_triag - triag_side * sin(pi / 2 * gamma / 90)
    penColor("red")
    brushColor("red")
    polygon([(x1_triag, y1_triag),
             (x2_triag, y2_triag),
             (x3_triag, y3_triag),
             (x1_triag, y1_triag)])
    r = triag_side // 3
    x1_circ = x3_triag + r * cos(pi / 4)
    y1_circ = y3_triag - r * sin(pi / 4)
    circle(x1_circ, y1_circ, r)
    x2_circ = x2_triag - r * cos(pi / 4)
    y2_circ = y2_triag - r * cos(pi / 4)
    circle(x2_circ, y2_circ, r)

def iceCreamOnLine(Width, Height, x_point_touch, y_point_touch):
    penColor("black")
    x2_stick = x_point_touch - 10
    y2_stick = y_point_touch - 100
    line(x_point_touch, y_point_touch, x2_stick, y2_stick)
    iceCream(Width, Height, x2_stick, y2_stick)

Width = 500
Height = 400
windowSize(Width,Height)


#---------------ФОН-------------------
#голубой верх
brushColor(66,170, 255)
penColor(66,170, 255)
rectangle(0,0, Width, Height//2)
#зелёный низ
brushColor(000,255, 100)
penColor(000,255, 100)
rectangle(0,Height//2, Width, Height)
#------------------------------------



#точка касания рук
x_point_touch = Width//4
y_point_touch = Height*7//12

R_head = Width//14 #радиус голов
color_head = "white"

#---------------ПАРЕНЬ-------------------
menL(Width//2,Height,x_point_touch,y_point_touch,R_head,color_head, 0)

#---------------ДЕВУШКА-------------------
girlL(Width//2,Height,x_point_touch,y_point_touch,R_head,color_head, 0)

#---------------ПАРЕНЬ-------------------
menR(Width//2,Height,x_point_touch + Width//2,y_point_touch,R_head,color_head, Width//6*4)

#---------------ДЕВУШКА-------------------
girlR(Width//2,Height,x_point_touch+Width//2,y_point_touch,R_head,color_head, Width//4)

#---------------МОРОЖЕННОЕ-------------------
iceCream(Width//2, Height, x_point_touch - Width//6, y_point_touch)

#---------------шарик-------------------
ball(Width//2, Height, x_point_touch + Width//6*4 , y_point_touch)

#---------------МОРОЖЕННОЕнаПАЛОЧКЕ-------------------
iceCreamOnLine(Width//2, Height, x_point_touch + Width//4.5 , y_point_touch - Height*2//12 )

run()
