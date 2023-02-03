# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     temp = (color.rgb.r, color.rgb.b, color.rgb.g)
#     rgb_colors.append(temp)

#requirements
#print this on a 10 x 10 dot axis
#20 in size and spaced at 50

import turtle as t

color_pallet = [(202, 110, 164), (149, 50, 75), (222, 136, 201), (53, 123, 93), (170, 41, 154), (138, 20, 31),
                (134, 184, 163), (197, 73, 92), (47, 86, 121), (73, 35, 43), (145, 149, 178), (14, 70, 98),
                (232, 165, 176), (160, 158, 142), (54, 50, 45), (101, 77, 75), (183, 171, 205), (36, 74, 60),
                (19, 89, 86),  (82, 129, 148), (147, 19, 17), (27, 102, 68), (12, 64, 70), (107, 153, 127),
                (176, 208, 192), (168, 102, 99)]

brush = t.Turtle()

screen = t.Screen()
screen.exitonclick()
