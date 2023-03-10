# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     temp = (color.rgb.r, color.rgb.b, color.rgb.g)
#     rgb_colors.append(temp)

import random
import turtle as t

# requirements
# print this on a 10 x 10 dot axis
# 20 in size and spaced at 50
color_pallet = [(202, 110, 164), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31),
                (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98),
                (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60),
                (19, 89, 86), (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127),
                (176, 208, 192), (168, 102, 99)]


def next_row(brush,y_axis):
    brush.penup()
    brush.setpos(-200, y_axis)


def paint_row(brush):
    for x in range(10):
        brush.color(random.choice(color_pallet))
        brush.dot(20)
        brush.penup()
        if x == 9:
            continue
        brush.forward(50)
        brush.pendown()


def create_picture():
    brush = t.Turtle()
    t.colormode(255)
    brush.penup()
    brush.setpos(-200, -200)
    shift = -200
    for x in range(10):
        paint_row(brush)
        if x == 9:
            brush.hideturtle()
        shift += 50
        next_row(brush,shift)
create_picture()
screen = t.Screen()
screen.exitonclick()
